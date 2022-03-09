def test_purchase_more_places_than_points(
        client,
        load_clubs,
        load_competitions
        ):
    """ Test réservation plus de places que les points permettent """
    response = client.post(
        '/purchasePlaces',
        data={
            'competition': 'Competition Test',
            'club': 'Club Test',
            'places': '9'
            }
        )
    assert response.status_code == 200
    assert b'Sorry, you required more places '\
        b'than possible - Try again' in response.data


def test_purchase_more_than_12_places(
        client,
        load_clubs,
        load_competitions
        ):
    """ Test réservation plus de places que limite """
    response = client.post(
        '/purchasePlaces',
        data={
            'competition': 'Competition Test',
            'club': 'Club Test',
            'places': '13'
            }
        )
    assert response.status_code == 200
    assert b'Sorry, you only can book 12 '\
        b'places maximum - Try again' in response.data


def test_purchase_negative_places(
        client,
        load_clubs,
        load_competitions
        ):
    """ Test réservation avec nombre négatif de places """
    response = client.post(
        '/purchasePlaces',
        data={
            'competition': 'Competition Test',
            'club': 'Club Test',
            'places': '-3'
            }
        )
    assert response.status_code == 200
    assert b'Sorry, you must choose a positive '\
        b'number of places - Try again' in response.data


def test_purchase_for_passed_competition(
        client,
        load_clubs,
        load_competitions
        ):
    """ Test réservation pour compétition passée """
    response = client.get(
        '/book/Passed Test/Club Test',
        data={
            'competition': 'Passed Test',
            'club': 'Club Test',
            }
        )
    assert response.status_code == 200
    assert b'Sorry, this competition already took place - '\
        b'Select an other competition' in response.data


def test_purchase_with_success(
        client,
        load_clubs,
        load_competitions
        ):
    """ Test réservation avec succès """
    response = client.post(
        '/purchasePlaces',
        data={
            'competition': 'Competition Test',
            'club': 'Club Test',
            'places': '2'
            }
        )
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data


def test_reflection_of_points_update(
        client,
        load_clubs,
        load_competitions
        ):
    """ Test répercussion réservation sur total de points """
    response = client.post(
        '/purchasePlaces',
        data={
            'competition': 'Competition Test',
            'club': 'Club Test',
            'places': '2'
            }
        )
    assert response.status_code == 200
    assert load_clubs[0]['points'] == 2
