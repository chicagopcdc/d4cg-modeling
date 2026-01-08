# scripts/utils/sheets_helper.py

import os, pickle, datetime, ezsheets
from googleapiclient.discovery import build

AUTH_DIR = "scripts/auth"
TOKEN_PATH = "token.pickle"
FORMAT_SHEET_ID = "1UDTMiw0LnLwqUBNc4O2_FAAX5UylCy-VXXRxEojK4IA"

def _chdir_auth():
    """Change into the auth dir and return the original dir so we can restore it."""
    orig_dir = os.getcwd()
    os.chdir(AUTH_DIR)
    return orig_dir

def get_spreadsheet(spreadsheet_id):
    """
    Open a Google Sheet via ezsheets, assuming creds live in scripts/auth.
    Returns an ezsheets.Spreadsheet.
    """
    orig_dir = _chdir_auth()
    try:
        ss = ezsheets.Spreadsheet(spreadsheet_id)
        ss.IGNORE_QUOTA = True
    finally:
        os.chdir(orig_dir)
    return ss


def get_sheets_service():
    """
    Build a Google Sheets v4 service using an existing token pickle
    (e.g., token-sheets.pickle) in scripts/auth.
    """
    orig_dir = _chdir_auth()
    try:
        with open(TOKEN_PATH, "rb") as f:
            creds = pickle.load(f)
        service = build("sheets", "v4", credentials=creds)
    finally:
        os.chdir(orig_dir)
    return service


def create_spreadsheet(title):
    """
    Create a brand-new Google Spreadsheet with the given title and
    return its spreadsheetId.
    """
    service = get_sheets_service()
    body = {"properties": {"title": title}}
    resp = service.spreadsheets().create(body=body).execute()
    return resp["spreadsheetId"]


def copy_formatting(target_spreadsheet_id, new_sheet_name):
    """
    Copy the sheet named template_sheet_name (default 'FORMATTING')
    from template_spreadsheet_id into target_spreadsheet_id,
    rename it to new_sheet_name, move it to index 0, and clear all values
    (keeping formatting).

    Returns the numeric sheetId of the new sheet in the target spreadsheet.
    """
    service = get_sheets_service()

    # 1. Find the FORMATTING sheet and ID
    src_meta = service.spreadsheets().get(
        spreadsheetId=FORMAT_SHEET_ID
    ).execute()
    template_sheet_id = None
    for sh in src_meta.get("sheets", []):
        props = sh.get("properties", {})
        if props.get("title") == "FORMATTING":
            template_sheet_id = props.get("sheetId")
            break
    if template_sheet_id is None:
        raise ValueError(
            f"Template sheet 'FORMATTING' not found in spreadsheet {FORMAT_SHEET_ID}"
        )

    # 2. Copy that sheet into the target spreadsheet
    copy_resp = service.spreadsheets().sheets().copyTo(
        spreadsheetId=FORMAT_SHEET_ID,
        sheetId=template_sheet_id,
        body={"destinationSpreadsheetId": target_spreadsheet_id},
    ).execute()

    new_sheet_id = copy_resp["sheetId"]

    # 3. Rename the copied sheet and move it to index 0
    service.spreadsheets().batchUpdate(
        spreadsheetId=target_spreadsheet_id,
        body={
            "requests": [
                {
                    "updateSheetProperties": {
                        "properties": {
                            "sheetId": new_sheet_id,
                            "title": new_sheet_name,
                            "index": 0,
                        },
                        "fields": "title,index",
                    }
                }
            ]
        },
    ).execute()

    # 4. Clear values only (keep formatting)
    service.spreadsheets().values().clear(
        spreadsheetId=target_spreadsheet_id,
        range=new_sheet_name,
        body={},
    ).execute()

    return new_sheet_id


def create_formatted_sheet(subset, spreadsheet_id):
    """
    Create a new sheet in spreadsheet_id named 'YYYYMMDD subset',
    using a formatting template sheet from template_spreadsheet_id.

    If a sheet with that name already exists, it is deleted first.

    Returns the ezsheets.Sheet object for the new sheet.
    """
    name = datetime.datetime.now().strftime("%Y%m%d") + " " + subset

    # Delete any old sheet with this name
    ss = get_spreadsheet(spreadsheet_id)
    existing_sheet = next((s for s in ss.sheets if s.title == name), None)
    if existing_sheet:
        print("...deleting existing sheet with same name (from an earlier run today)")
        existing_sheet.delete()

    # Copy formatting sheet into target and rename
    copy_formatting(spreadsheet_id, name)

    # Re-open and return the new sheet
    ss = get_spreadsheet(spreadsheet_id)
    return ss[name]


def upsert_plain_sheet(spreadsheet_id, sheet_name, rows):
    """
    Create or replace a sheet named sheet_name in the given spreadsheet
    with no special formatting (just ezsheets.createSheet) and write rows.
    """
    ss = get_spreadsheet(spreadsheet_id)
    existing_sheet = next((s for s in ss.sheets if s.title == sheet_name), None)
    if existing_sheet:
        existing_sheet.delete()
    sheet = ss.createSheet(sheet_name)
    # Ensure rectangular data
    max_len = max(len(r) for r in rows)
    normalized_rows = []
    for r in rows:
        r = list(r)  # in case it's a tuple or similar
        if len(r) < max_len:
            r = r + [""] * (max_len - len(r))
        normalized_rows.append(r)
    # Safety check – all rows must have same length
    assert all(len(r) == max_len for r in normalized_rows), (
        f"Non-rectangular data for {str(r)}"
    )
    # Write one row at a time to avoid updateRows IndexError
    for row_idx, row_values in enumerate(normalized_rows, start=1):
        sheet.updateRow(row_idx, row_values)
    
    return sheet


def create_spreadsheet_from_tables(title, sheets, folder_id):
    """
    Create a Google Spreadsheet populated with the given sheets and move it
    into the specified Drive folder.
      - If a spreadsheet with the same title already exists IN THAT FOLDER,
        delete it first.
      - Then create a new spreadsheet, populate tabs, and move it into
        the folder.
    Returns the new spreadsheetId.
    """
    # Get creds once and build Drive + Sheets services off of them
    sheets_service = get_sheets_service()
    creds = sheets_service._http.credentials
    drive_service = build("drive", "v3", credentials=creds)

    # 1. Delete any existing spreadsheet with this title in the target folder
    query = (
        f"name = '{title}' and "
        f"'{folder_id}' in parents and "
        "mimeType = 'application/vnd.google-apps.spreadsheet' and "
        "trashed = false"
    )
    existing = drive_service.files().list(
        q=query,
        fields="files(id, name)",
        corpora="allDrives",
        includeItemsFromAllDrives=True,
        supportsAllDrives=True
    ).execute()

    for f in existing.get("files", []):
        print(f"...a duplicate file from a previous run today was found, will move that file to trash to avoid a duplicate\n")
        drive_service.files().update(
                fileId=f["id"],
                body={"trashed": True},
                fields="id, trashed",
                supportsAllDrives=True
            ).execute()

    # 2. Create spreadsheet (still via Sheets API helper)
    print("...creating new spreadsheet")
    spreadsheet_id = create_spreadsheet(title)

    # 3. Add all sheets (tabs)
    for sheet_name, rows in sheets.items():
        if rows:
            print("...adding new sheet for: " + sheet_name)
            upsert_plain_sheet(spreadsheet_id, sheet_name, rows)
    
    # Remove the blank default sheet
    ss = get_spreadsheet(spreadsheet_id)
    default_sheet = next((s for s in ss.sheets if s.title == "Sheet1"), None)
    if default_sheet:
        print("...deleting default Sheet1")
        default_sheet.delete()

    # 4. Move the file into the target folder
    file_meta = drive_service.files().get(
        fileId=spreadsheet_id,
        fields="parents",
        supportsAllDrives=True
    ).execute()
    prev_parents = ",".join(file_meta.get("parents", []))

    drive_service.files().update(
        fileId=spreadsheet_id,
        addParents=folder_id,
        removeParents=prev_parents,
        fields="id,parents",
        supportsAllDrives=True
    ).execute()

    return spreadsheet_id