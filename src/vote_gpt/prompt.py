from openai import OpenAI


def create_search_query(question:str):
    """Use GPT3 to create a search query"""

    prompt = f"Create a search engine query for me to answer the following question: {question}"
    return call_gpt(prompt)

def process_search_results(results:str, question:str):
    prompt = f"""
    {results} \n above are search results about
    voting laws in the US. Answer the following question from the search results:
    '{question}'.
    Please...
    * emphasize official information and specific procedures,
    * provide links, phone numbers, and email addresses if available
    """
    return call_gpt(prompt)

def call_gpt(query:str):
    """Retrieve a response from gpt"""

    instructions = """
    You are a master summarizer of complex, hard to understand information about the year 2024.
    """
    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "content": query},
    ]
    )
    return response.choices[0].message.content.strip('\"') + "\n"