from lib.database_connection import DatabaseConnection


SEED_FILE = "seeds/setup_seed_tables.sql"


def use_test_database(monkeypatch):
    monkeypatch.setattr(
        DatabaseConnection,
        "DEV_DATABASE_NAME",
        DatabaseConnection.TEST_DATABASE_NAME,
    )

def log_in_test_user(web_client):
    with web_client.session_transaction() as test_session:
        test_session["user_id"] = 1
        test_session["email"] = "kayleighk@kickabout.com"


def test_create_listing_page_displays_the_form(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)
    log_in_test_user(web_client)

    response = web_client.get("/listings/new")

    assert response.status_code == 200
    assert b"Create a Listing" in response.data
    assert b'name="title"' in response.data
    assert b'name="description"' in response.data
    assert b'name="price"' in response.data
    assert b'name="available_from"' in response.data
    assert b'name="available_until"' in response.data
    assert b"Create Listing" in response.data


def test_creating_a_listing_saves_it_to_the_database(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)
    log_in_test_user(web_client)

    response = web_client.post(
        "/listings/new",
        data={
            "title": "Canal-side studio",
            "description": "A compact studio overlooking the canal.",
            "price": "125",
            "available_from": "2026-09-01",
            "available_until": "2026-09-30",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/listings")

    rows = db_connection.execute(
        """
        SELECT *
        FROM listings
        WHERE title = %s
        """,
        ["Canal-side studio"],
    )

    assert len(rows) == 1
    assert rows[0]["owner_id"] == 1
    assert rows[0]["description"] == (
        "A compact studio overlooking the canal."
    )
    assert rows[0]["price_per_night"] == 125


def test_created_listing_appears_on_the_listings_page(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)
    log_in_test_user(web_client)

    response = web_client.post(
        "/listings/new",
        data={
            "title": "Canal-side studio",
            "description": "A compact studio overlooking the canal.",
            "price": "125",
            "available_from": "2026-09-01",
            "available_until": "2026-09-30",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.request.path == "/listings"
    assert b"Canal-side studio" in response.data
    assert b"A compact studio overlooking the canal." in response.data
    assert b"125 per night" in response.data


def test_signed_out_user_is_redirected_from_create_listing_page(
    web_client,
    monkeypatch,
):
    use_test_database(monkeypatch)

    response = web_client.get(
        "/listings/new",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/users/login")