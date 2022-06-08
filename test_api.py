from httpx import get


class TestDeckOfCards:
    """Set of tests for Deck of Cards API."""

    def __init__(self):
        base_url = "http://deckofcardsapi.com/api/deck/"

    def test_return_200(self):
        """Test if the endpoint returns http status 200."""
        request = get(self.base_url)
        assert request.status_code == 200
