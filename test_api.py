from httpx import get


class TestDeckOfCards:
    """Set of tests for Deck of Cards API."""

    base_url = "http://deckofcardsapi.com/api/deck/"

    def test_return_200(self):
        """Test if the endpoint returns http status 200."""
        request = get(self.base_url + "new/shuffle/")
        assert request.status_code == 200
