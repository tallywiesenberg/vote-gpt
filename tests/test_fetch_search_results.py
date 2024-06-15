from src.vote_gpt.main import call_gpt2, create_search_query, fetch_search_results, process_search_results
import pytest

def test_create_search_query():

    question = "What's on the ballot in Florida in 2024?"

    assert "ballot" in create_search_query(question)
    assert "Florida" in create_search_query(question)


def test_call_gpt():

    response = call_gpt2("What is GPT?")
    assert len(response) > 1
    assert "GPT" in response

    simple_prompt = "Once upon a time"
    simple_response = call_gpt2(simple_prompt)
    assert simple_prompt != simple_response

def test_fetch_search_results():
    
    results = fetch_search_results("voting in Wisconsin")
    length = len(results)

    assert length > 1
    assert "Wisconsin" in results

def test_process_search_results():

    question = "When can I vote in Colorado in 2024?"
    
    topics = create_search_query(question)
    results = fetch_search_results("Voting in Colorado")
    processed_results = process_search_results(results, topics, question)
    print(processed_results)