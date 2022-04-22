from __future__ import print_function

import json
import base64
import sys
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/contacts']


def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('people', 'v1', credentials=creds)


def upload_one_photo(name, photo_file):
    service = get_service()

    search_result = service.people().searchContacts(query=name, readMask='names').execute()
    resource_name = search_result['results'][0]['person']['resourceName']

    JSON = """{
        "photoBytes": "%s"
    }
    """ % (base64.b64encode(open(photo_file, "rb").read()).decode('utf-8'))
    update_body = json.loads(JSON)

    service.people().updateContactPhoto(resourceName=resource_name, body=update_body).execute()
    print("Updated " + name)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 " + sys.argv[0] + " <name> <photo_file>")
        sys.exit(1)

    name = sys.argv[1]
    photo_file = sys.argv[2]

    print("Uploading photo for name={" + name + "} photo_file={" + photo_file + "}")
    upload_one_photo(name, photo_file)


if __name__ == '__main__':
    main()
