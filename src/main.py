import requests
import huggingface
from googleapiclient.discovery import build

from dotenv import load_dotenv
import os

load_dotenv()

def fetch_voter_registration_info():

    g_api_key = os.getenv("GOOGLE_API_KEY")
    g_cse_key = os.getenv("GOOGLE_SEARCH_API")

    # Build the Google Custom Search Engine service object.
    service = build("customsearch", "v1", developerKey=g_api_key)

    # Define the search query.
    query = "voter registration information"

    # Perform the search.
    response = service.cse().list(
        q=query, cx=g_cse_key
    ).execute()

    # Extract the search results.
    items = response.get("items", [])

    # Return the search results.
    return items
