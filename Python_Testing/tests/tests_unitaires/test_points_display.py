def test_points_presentation(client, load_clubs):
    """ Test présentation du tableau des points """
    response = client.get('/points_display')
    assert response.status_code == 200
    assert b'<td> Club Test </td>' in response.data
    assert b'<td> 8 </td>' in response.data
