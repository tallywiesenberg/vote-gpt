import os
from googleapiclient.discovery import build
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def fetch_search_results(query:str) -> str:
    """search google and return the results as a string"""

    g_api_key = os.getenv("GOOGLE_API_KEY")
    g_cse_key = os.getenv("GOOGLE_SEARCH_API")

    # Build the Google Custom Search Engine service object.
    service = build("customsearch", "v1", developerKey=g_api_key)

    # Perform the search.
    response = service.cse().list(
        q=query, cx=g_cse_key, num=10
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

def search_tavily(query):
    """Search LLM friendly search engine Tavily"""

    tavily = TavilyClient(api_key=os.getenv("TAVILY_API"))
    response = tavily.search(query=query, search_depth="advanced")
    # Get the search results as context to pass an LLM:
    return [
        {"url": obj["url"], "content": obj["content"]}
         for obj in response["results"]
         if any(x in obj["url"] for x in[".org", ".gov"]) # restrict to trustworthy websites
    ]