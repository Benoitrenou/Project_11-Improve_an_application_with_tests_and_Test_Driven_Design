import server
from tests.conftest import client


def test_login_with_wrong_email(client):
    response = client.post(
        "/showSummary",
        data={'email':'test@wrnogemail.com'},
        follow_redirects=True
        )
    assert response.status_code == 200
    assert b'Email not found - Please try again' in response.data

def test_login(client):
    response = client.post(
        "/showSummary",
        data={'email':'john@simplylift.co'},
        follow_redirects=True
        )
    assert response.status_code == 200
    assert b'Summary | GUDLFT Registration' in response.data

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
    response = client.get('/')
    assert response.status_code == 200
    assert b'Club : Club Test / Points : 15' in response.data
