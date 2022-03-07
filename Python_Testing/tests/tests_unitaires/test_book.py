import server
import pytest
from tests.conftest import client

""" def test_error_book(client):
    response = client.get(
        '/book/Competition Test/Club Test',
        data={
            'competition': 'Competition Test',
            'club': 'Club Test',
            }
        )
    print(response.data.decode())
    assert response.status_code == 200
    assert b'Something went wrong-please try again' in response.data """

def test_success_book(client, mocker):
    mocker.patch.object(
        server,
        'clubs',
        [{
            "name":"Club Test",
            "email":"secretary@clubtest.com",
            "points":"8"
            }]
        )
    mocker.patch.object(
        server,
        'competitions',
        [{
            "name":"Competition Test",
            "date":"2022-03-27 10:00:00",
            "numberOfPlaces":"12"
            }]
        )
    response = client.get(
            '/book/Competition Test/Club Test',
            data={
                'competition': 'Competition Test',
                'club': 'Club Test',
                }
            )
    assert response.status_code == 200
    assert b'Booking for Competition Test' in response.data
