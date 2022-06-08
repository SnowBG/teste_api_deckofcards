from httpx import get


class TestDeckOfCards:
    """Set of tests for Deck of Cards API."""

    base_url = "http://deckofcardsapi.com/api/deck/"

    def test_new_deck_return_200(self):
        """Test if the endpoint returns http status 200."""
        request = get(self.base_url + "new/")
        assert request.status_code == 200
        return request

    def test_new_deck_return_json(self):
        """Test if the endpoint returns a JSON."""
        request = get(self.base_url + "new/")
        assert request.json() is not None
        return request

    def test_new_shuffle_deck_return_200(self):
        """Test if the endpoint returns http status 200."""
        request = get(self.base_url + "new/shuffle/")
        assert request.status_code == 200
        return request

    def test_shuffle_deck_return_json(self):
        """Test if the endpoint returns a JSON"""
        request = get(self.base_url + "new/shuffle/")
        assert request.json() is not None
        return request

    def test_new_deck_content(self):
        """Test if the JSON content is correct"""
        request = get(self.base_url + "new/")
        assert request.json()['success'] is True
        assert len(request.json()['deck_id']) == 12
        assert request.json()['remaining'] == 52
        assert request.json()['shuffled'] is False
        return request

    def test_new_shuffle_deck_content(self):
        """Test if the JSON content is correct"""
        request = get(self.base_url + "new/shuffle/")
        assert request.json()['success'] is True
        assert len(request.json()['deck_id']) == 12
        assert request.json()['remaining'] == 52
        assert request.json()['shuffled'] is True
        return request
