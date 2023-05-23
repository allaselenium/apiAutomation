import pytest
import requests


@pytest.mark.jsonplaceholdertest
def test_post_request():
    my_obj = {
        "userId": 1,
        "id": 1,
        "title": 'foo',
        "body": 'bar'
    }

    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=my_obj)
    assert response.status_code == 200
