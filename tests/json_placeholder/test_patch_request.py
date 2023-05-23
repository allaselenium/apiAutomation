import pytest
import requests


@pytest.mark.jsonplaceholdertest
def test_post_request():
    my_obj ={
        "title": "my updated title"
    }
    response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", data=my_obj)
    assert response.status_code == 200




