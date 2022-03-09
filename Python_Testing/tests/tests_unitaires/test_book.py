def test_success_book(
        client,
        load_clubs,
        load_competitions
        ):
    """ Test accès à réservation avec succès """
    response = client.get(
            '/book/Competition Test/Club Test',
            data={
                'competition': 'Competition Test',
                'club': 'Club Test',
                }
            )
    print(response.data.decode())
    assert response.status_code == 200
    assert b'Booking for Competition Test' in response.data


def test_error_book(
        client,
        load_clubs,
        load_competitions
        ):
    """ Test accès à réservation avec erreur """
    response = client.get(
            '/book/Wrong Competition/Club Test',
            data={
                'competition': 'Wrong Competition',
                'club': 'Club Test',
                }
            )
    print(response.data.decode())
    assert response.status_code == 200
    assert b'Something went wrong-please try again' in response.data
