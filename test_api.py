from httpx import get


class TestDeckOfCards:
    """Set of tests for Deck of Cards API."""

    base_url = "http://deckofcardsapi.com/api/deck/"

    def test_new_deck_return_200(self):
        """Test if the endpoint returns http status 200."""
        request = get(f"{self.base_url}/new/")
        assert request.status_code == 200

    def test_new_deck_return_json(self):
        """Test if the endpoint returns a JSON."""
        request = get(f"{self.base_url}/new/")
        assert request.json() is not None

    def test_new_shuffle_deck_return_200(self):
        """Test if the endpoint returns http status 200."""
        request = get(f"{self.base_url}/new/shuffle/")
        assert request.status_code == 200

    def test_shuffle_deck_return_json(self):
        """Test if the endpoint returns a JSON."""
        request = get(f"{self.base_url}/new/shuffle/")
        assert request.json() is not None

    def test_new_deck_content(self):
        """Test if the JSON content is correct."""
        request = get(f"{self.base_url}/new/")
        assert request.json()['success'] is True
        assert len(request.json()['deck_id']) == 12
        assert request.json()['remaining'] == 52
        assert request.json()['shuffled'] is False

    def test_new_shuffle_deck_content(self):
        """Test if the JSON content is correct."""
        request = get(f"{self.base_url}/new/shuffle/")
        assert request.json()['success'] is True
        assert len(request.json()['deck_id']) == 12
        assert request.json()['remaining'] == 52
        assert request.json()['shuffled'] is True

    def test_draw_3_cards(self):
        """Test draw 3 cards from deck."""
        request = get(f"{self.base_url}/new/shuffle/")
        deck_id = request.json()['deck_id']
        request_draw = get(f"{self.base_url}/{deck_id}/draw/?count=3")
        assert request_draw.status_code == 200
        assert request_draw.json()['success'] is True
        assert request_draw.json()['deck_id'] == deck_id
        assert len(request_draw.json()['cards']) == 3
