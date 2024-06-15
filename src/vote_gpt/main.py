from googleapiclient.discovery import build
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from dotenv import load_dotenv
import os

load_dotenv()

def create_search_query(user_question:str):
    """Create a search query from a user's question"""

    return call_gpt2(f"""
                     Create a search engine query for the user's question: {user_question}.
                      The goal of the search is for the user to understand complex documents, procedures, and information.
                      """)

    

def fetch_search_results(query:str):

    g_api_key = os.getenv("GOOGLE_API_KEY")
    g_cse_key = os.getenv("GOOGLE_SEARCH_API")

    # Build the Google Custom Search Engine service object.
    service = build("customsearch", "v1", developerKey=g_api_key)

    # Perform the search.
    response = service.cse().list(
        q=query, cx=g_cse_key
    ).execute()

    # Extract the search results.
    items = response.get("items", [])

    formatted_results = []
    for item in items:
        title = item.get("title")
        snippet = item.get("snippet")
        link = item.get("link")
        formatted_results.append(f"Title: {title}\nSnippet: {snippet}\nLink: {link}\n")
    return "\n\n".join(formatted_results)

def process_search_results(results:str , core_topic:str, question:str):
    return call_gpt2(f"""
                                {results} \n above are search results about
                                {core_topic}. Answer the following question from the search results:
                                '{question}' Let me know the certainty of your answer on a scale of 1-10.
""")

def call_gpt(query:str):
    """Retrieve a response from gpt4"""