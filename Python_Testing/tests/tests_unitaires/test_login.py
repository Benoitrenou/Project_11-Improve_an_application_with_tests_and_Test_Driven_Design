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
