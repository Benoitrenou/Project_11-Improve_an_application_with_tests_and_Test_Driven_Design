def test_login_logout_route(client, load_clubs):
    response = client.post(
        "/showSummary",
        data={'email':'secretary@clubtest.com'},
        follow_redirects=True
        )
    assert response.status_code == 200
    assert b'Summary | GUDLFT Registration' in response.data
    response = client.get('/logout')
    assert response.status_code == 302
    assert b'<h1>Redirecting...</h1>' in  response.data

def test_book_competition_route(client, load_clubs, load_competitions):
    client.post(
        "/showSummary",
        data={'email':'secretary@clubtest.com'},
        follow_redirects=True
        )
    client.get('/book/Competition Test/Club Test')
    response = client.post(
        'purchasePlaces',
        data=dict(places=2, club='Club Test', competition='Competition Test')
        )
    assert b'Great-booking complete!' in response.data
    assert load_clubs[0]['points'] == 6
