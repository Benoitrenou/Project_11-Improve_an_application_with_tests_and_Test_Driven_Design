import server
from tests.conftest import client


def test_points_presentation(client, mocker):
    club = mocker.patch.object(
        server,
        'clubs',
        [{
            "name":"Club Test",
            "email":"secretary@clubtest.com",
            "points":"15"
            }]
        )
    response = client.get('/points_display')
    assert response.status_code == 200
    assert b'<td> Club Test </td>' in response.data
    assert b'<td> 15 </td>' in response.data
