from openai import OpenAI


def create_search_query(question:str):
    """Use GPT3 to create a search query"""

    prompt = f"Create a search engine query for me to answer the following question: {question}"
    return call_gpt(prompt)

def process_search_results(results:str, question:str):
    prompt = f"""
    {results} \n above are search results about
    voting laws in the US. Answer the following question from the search results:
    '{question}' Let me know the certainty of your answer on a scale of 1-10.
    """
    return call_gpt(prompt)

instructions = """
You are a master summarizer of complex, hard to understand information.
"""

def call_gpt(query:str):
    """Retrieve a response from gpt"""

    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "content": query},
    ]
    )
    return response.choices[0].message.content