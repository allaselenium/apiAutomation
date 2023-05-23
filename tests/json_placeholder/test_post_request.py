import pytest
import requests


@pytest.mark.jsonplaceholdertest
def test_post_request():
    my_obj ={
        "userId": 1,
        "title": "my title",
        "body": "body example"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", data=my_obj)
    assert response.status_code == 201




