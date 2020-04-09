from testapp.app import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_index_page(client):
    result = client.get('/')
    print(result.data)
    assert b'<html>' in result.data
    assert result.status_code == 200


def test_index_page(client):
    result = client.post(
        '/login_processor',
        data={'username': 'guest', 'password': '12345'},
        follow_redirects=True
    )
    assert result.status_code == 200
