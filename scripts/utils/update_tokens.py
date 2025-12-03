from __future__ import print_function
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow

AUTH_DIR = "scripts/auth"
CREDENTIALS_FILE = os.path.join(AUTH_DIR, "credentials-sheets.json")
TOKEN_PATH = os.path.join(AUTH_DIR, "token-sheets.pickle")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",  # full Drive access (needed for search/move/delete)
]

def main():
    os.makedirs(AUTH_DIR, exist_ok=True)

    if not os.path.exists(CREDENTIALS_FILE):
        raise SystemExit(f"Missing {CREDENTIALS_FILE}")

    # Start clean
    if os.path.exists(TOKEN_PATH):
        os.remove(TOKEN_PATH)

    flow = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_FILE,
        SCOPES,
    )

    # Force a full new consent so we definitely get a refresh_token
    creds = flow.run_local_server(
        port=8080,
        access_type="offline",
        prompt="consent",
    )

    with open(TOKEN_PATH, "wb") as token:
        pickle.dump(creds, token)

    print(f"New token written to {TOKEN_PATH}")
    # Optional sanity check:
    if not creds.refresh_token:
        print("WARNING: refresh_token is still missing.")

if __name__ == "__main__":
    main()