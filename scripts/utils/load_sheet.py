# scripts/utils/load_sheet.py

import re
from utils.sheets_helper import get_spreadsheet


def load(gsheet_id, subset):
    """
    Find and return the sheet in gsheet_id whose info/Name == subset.
    """
    ss = get_spreadsheet(gsheet_id)
    if ss is None:
        print("Could not load sheet for subset: " + subset)
        return None

    # Look through all sheets in the dictionary
    for sheet in ss.sheets:
        rows = sheet.getRows()
        for i in range(len(rows)):
            line = rows[i]
            if line[0] in ["info", "INFO"]:
                # Only load the target version sheet (single)
                if line[1] == "Name" and line[2] == subset:
                    return sheet

            if line[0] in ["domain", "DD"]:
                # Once we hit the first domain/table rows, we can stop scanning this sheet
                break

    # If nothing matched:
    return None


def parse(sheet):
    dictionary = {"info": {}, "tables": []}
    # Track the "current" domain, table, and variable
    current_domain, current_table, current_var, var_num = "", None, None, 0
    # Get all rows of the sheet
    rows = sheet.getRows()
    for i in range(len(rows)):
        line = rows[i]
        # Use the different RowTypes to send this line to be processed
        if line[0] in ["info", "INFO"]:
            if line[1] == "Title":
                dictionary["info"]["title"] = line[2]
            if line[1] == "Name":
                dictionary["info"]["name"] = line[2]
            if line[1] == "Release Notes":
                dictionary["info"]["release_note"] = line[2]
            if line[1] in ["Parent Data Model", "Parent Model"]:
                dictionary["info"]["parent_model"] = line[2]
            if line[1] == "Description":
                dictionary["info"]["description"] = line[2]
        if line[0] in ["domain", "DD"]:
            current_domain = check_field(dictionary["info"]["name"], line, 1, "domain name", i)
            current_domain = current_domain.replace(" ", "_").lower()
        if line[0] in ["table", "TD"]:
            if current_table is not None:
                #Add the now completely check_fieldd table to the dictionary object
                current_table["variables"].append(current_var)
                current_var = None
                dictionary["tables"].append(current_table)
            #Create a new table
            table_name = check_field(dictionary["info"]["name"], line, 1, "table name", i).replace(" ", "")
            current_table = {
                "name": table_name,
                "domain": current_domain,
                "implementation_notes": re.split(r'[|\n]', check_field(dictionary["info"]["name"], line, 9, "ImplementationNotes", i)),
                "mappings": [m.strip() for m in check_field(dictionary["info"]["name"], line, 10, "Mappings", i).split("|") if m.strip()],
                "variables": []
            }
        if line[0] in ["var", "VD"]:
            var_num += 1
            var_name = check_field(dictionary["info"]["name"], line, 1, "VariableName", i)
            if current_var is not None:
                #Add the now completely check_field variable to the table object
                current_table["variables"].append(current_var)
            current_var = {
                "name": var_name.lower(),
                "type": check_field(dictionary["info"]["name"], line, 2, "DataType", i).lower(),
                "tier": check_field(dictionary["info"]["name"], line, 3, "Tier", i).lower(),
                "code": check_field(dictionary["info"]["name"], line, 5, "VariableCode", i).split("|")[0].strip(),
                "implementation_notes": re.split(r'[|\n]', check_field(dictionary["info"]["name"], line, 9, "ImplementationNotes", i)),
                "mappings": [m.strip() for m in check_field(dictionary["info"]["name"], line, 10, "Mappings", i).split("|") if m.strip()],
                "permissible_values": []
            }
        if line[0] in ["pv", "PD"]:
            current_var["permissible_values"].append({
                "value": check_field(dictionary["info"]["name"], line, 6, "PermissibleValue", i),
                "code": check_field(dictionary["info"]["name"], line, 8, "ValueCode", i).split("|")[0].strip(),
                "implementation_notes": re.split(r'[|\n]', check_field(dictionary["info"]["name"], line, 9, "ImplementationNotes", i)),
                "mappings": [m.strip() for m in check_field(dictionary["info"]["name"], line, 10, "Mappings", i).split("|") if m.strip()]
            })

    dictionary["info"]["total_variables"] = var_num
    return dictionary


def check_field(d, line, idx, target, row):
    try:
        return line[idx]
    except IndexError:
        error = "Missing \"" + target + "\" for parsing on line " + str(row + 1) + " of dictionary: " + d
        print(error)
        return error