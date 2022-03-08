def test_login_with_wrong_email(client):
    response = client.post(
        "/showSummary",
        data={'email':'test@wrongemail.com'},
        follow_redirects=True
        )
    assert response.status_code == 200
    assert b'Email not found - Please try again' in response.data

def test_login(client, load_clubs):
    response = client.post(
        "/showSummary",
        data={'email':'secretary@clubtest.com'},
        follow_redirects=True
        )
    assert response.status_code == 200
    assert b'Summary | GUDLFT Registration' in response.data

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in  response.data

def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302
    assert b'<h1>Redirecting...</h1>' in  response.data
