import pytest
import server
from server import app


@pytest.fixture
def client():
    """ Fixture du client pour tests """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def load_clubs(mocker):
    """ Fixture données clubs pour tests """
    return mocker.patch.object(
            server,
            'clubs',
            [{
                "name": "Club Test",
                "email": "secretary@clubtest.com",
                "points": "8"
                }]
            )


@pytest.fixture
def load_competitions(mocker):
    """ Fixture données compétititons pour tests """
    return mocker.patch.object(
            server,
            'competitions',
            [
                {
                    "name": "Competition Test",
                    "date": "2022-03-27 10:00:00",
                    "numberOfPlaces": "12"
                },
                {
                    "name": "Passed Test",
                    "date": "2020-03-27 10:00:00",
                    "numberOfPlaces": "12"
                }
                ]
            )
