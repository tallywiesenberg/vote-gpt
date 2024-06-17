"""Test google sheets integration."""

from src.vote_gpt.forms import get_google_sheets_data


def test_google_sheets_request():
    """Test google sheets request."""
    rows = get_google_sheets_data()
    assert rows is not None
    assert len(rows) > 0
