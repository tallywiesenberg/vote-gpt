from src.vote_gpt.main import call_gpt, create_search_query, fetch_search_results, process_search_results
import pytest


def test_call_gpt():

    response = call_gpt("Colarado")
    assert len(response) > 1
    assert "Colorado" in response

    simple_prompt = "Once upon a time"
    simple_response = call_gpt(simple_prompt)
    assert simple_prompt != simple_response

def test_fetch_search_results():
    
    results = fetch_search_results("voting in Wisconsin")
    length = len(results)

    assert length > 1
    assert "Wisconsin" in results

def test_create_search_query():

    question = "Can I take off from work to vote in Colorado?"
    response = create_search_query(question)
    assert len(response) < 50


def test_process_search_results():

    question = "Can I take off from work to vote in Colorado?"
    prompt = "Colorado voting leave laws for employees"
    results = fetch_search_results(prompt)
    processed_results = process_search_results(results, question)
    print(processed_results)