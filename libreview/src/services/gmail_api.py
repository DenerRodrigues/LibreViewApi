import os
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src import settings


SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


class GmailAPI:
    def __init__(self):
        self.service = build("gmail", "v1", credentials=self.__get_credentials())

    @staticmethod
    def __get_credentials():
        credentials = None
        token_path = f"{settings.MEDIA_FILES_DIR}/gmail_token.json"

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(token_path):
            credentials = Credentials.from_authorized_user_file(token_path, SCOPES)
        else:
            raise Exception("Token file not found")

        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())

        return credentials

    def get_verification_code(self):
        try:
            # Call the Gmail API
            results = (
                self.service.users()
                .messages()
                .list(userId="me", q="Código de verificação LibreView")
                .execute()
            )
            messages = results.get("messages", [])

            if not messages:
                print("Not found emails from Libreview Code")
                return

            _code_list = []
            for m in messages[:3]:
                message_id = m["id"]

                _message = (
                    self.service.users()
                    .messages()
                    .get(userId="me", id=message_id)
                    .execute()
                )
                if not _message:
                    print("error getting message")
                    return
                snipped = _message["snippet"]
                code = re.search("(\d{6})", snipped).group()
                if not code:
                    continue

                print(f"Verification code: {code}")
                return code

        except HttpError as error:
            print(f"An error occurred: {error}")
