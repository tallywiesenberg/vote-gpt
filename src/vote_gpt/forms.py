"""Processing Google Form data"""

import os
import openai
import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Set up Google Sheets API credentials and service
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'  # Replace with your service account file path
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = 'your_spreadsheet_id'  # Replace with your Google Sheets ID
RANGE_NAME = 'Sheet1!A1:B10'  # Adjust the range based on your sheet structure

# Authenticate and construct the service
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

# OpenAI API key
openai.api_key = 'your_openai_api_key'  # Replace with your OpenAI API key

def get_google_sheets_data():
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    values = result.get('values', [])
    return values