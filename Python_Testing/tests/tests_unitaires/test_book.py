def test_success_book(
    client,
    load_clubs,
    load_competitions
    ):
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
