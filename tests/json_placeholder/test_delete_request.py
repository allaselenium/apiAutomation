import pytest
import requests


@pytest.mark.jsonplaceholdertest
def test_post_request():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200