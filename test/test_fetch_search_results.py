from src.main import fetch_voter_registration_info
import pytest

def test_fetch_search_results():

    assert "vote" in fetch_voter_registration_info("vote")