from googleapiclient.discovery import build
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()
assistant = client.beta.assistants.create(
  name="Voting Registration Assistant",
  instructions="You are an election volunteer. Find information about the election and retrieve relevant links, documents, and forms.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)

tools = [{
        "type": "function",
        "function": {
            "name": "fetch_search_results",
            "description": "Get voting instructions from the web.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query to use. For example: 'Latest news on Nvidia stock performance'"},
                },
                "required": ["query"]
            }
        }
    }]

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
    return call_gpt(f"""
                                {results} \n above are search results about
                                {core_topic}. Answer the following question from the search results:
                                '{question}' Let me know the certainty of your answer on a scale of 1-10.
""")

def call_gpt(location:str, ):
    """Retrieve a response from gpt"""

    client = OpenAI()
    assistant = client.beta.assistants.create(
    name="Voting Registration Assistant",
    instructions="You are an election volunteer. Find information about the election and retrieve relevant links, documents, and forms.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o",
    )

    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
    )

    run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account."
    )

    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        print(messages)
    else:
        print(run.status)

