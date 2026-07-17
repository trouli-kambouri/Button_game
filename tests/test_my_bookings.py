from lib.database_connection import DatabaseConnection


SEED_FILE = "seeds/setup_seed_tables.sql"


def use_test_database(monkeypatch):
    monkeypatch.setattr(
        DatabaseConnection,
        "DEV_DATABASE_NAME",
        DatabaseConnection.TEST_DATABASE_NAME,
    )


def log_in_user(
    web_client,
    user_id,
    email,
):
    with web_client.session_transaction() as test_session:
        test_session["user_id"] = user_id
        test_session["email"] = email


def test_signed_out_user_is_redirected_from_my_bookings(
    web_client,
    monkeypatch,
):
    use_test_database(monkeypatch)

    response = web_client.get(
        "/my_bookings",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith(
        "/users/login"
    )


def test_manage_bookings_page_displays_guest_and_owner_sections(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    log_in_user(
        web_client,
        5,
        "ttipple@taliastipples.co.uk",
    )

    response = web_client.get("/my_bookings")
    html = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "Manage Bookings" in html
    assert "My bookings" in html
    assert "My properties" in html


def test_manage_bookings_page_displays_the_users_booking(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    log_in_user(
        web_client,
        5,
        "ttipple@taliastipples.co.uk",
    )

    response = web_client.get("/my_bookings")
    html = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "Medieval castle with ghost included" in html
    assert "19-07-2026 - 20-07-2026" in html
    assert "Status: denied" in html


def test_manage_bookings_page_displays_request_for_owned_listing(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    log_in_user(
        web_client,
        5,
        "ttipple@taliastipples.co.uk",
    )

    response = web_client.get("/my_bookings")
    html = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "Beach hut only 5 days walk from beach" in html
    assert "12-07-2026 - 12-07-2026" in html
    assert "Status: requested" in html


def test_signed_out_user_cannot_create_a_booking(
    web_client,
    monkeypatch,
):
    use_test_database(monkeypatch)

    response = web_client.post(
        "/listings/12/my_bookings",
        data={
            "check_in": "2026-08-01",
            "check_out": "2026-08-03",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith(
        "/users/login"
    )


def test_signed_in_user_can_create_a_booking_request(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    log_in_user(
        web_client,
        2,
        "maming@matsforcats.co.uk",
    )

    response = web_client.post(
        "/listings/12/my_bookings",
        data={
            "check_in": "2026-08-01",
            "check_out": "2026-08-03",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith(
        "/my_bookings"
    )

    rows = db_connection.execute(
        """
        SELECT *
        FROM bookings
        WHERE listing_id = %s
          AND guest_id = %s
          AND start_date = %s
          AND end_date = %s
        """,
        [
            12,
            2,
            "2026-08-01",
            "2026-08-03",
        ],
    )

    assert len(rows) == 1
    assert rows[0]["status"] == "requested"


def test_booking_request_requires_both_dates(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    log_in_user(
        web_client,
        2,
        "maming@matsforcats.co.uk",
    )

    response = web_client.post(
        "/listings/12/my_bookings",
        data={
            "check_in": "2026-08-01",
            "check_out": "",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith(
        "/listings/12"
    )

    rows = db_connection.execute(
        """
        SELECT *
        FROM bookings
        WHERE listing_id = %s
          AND guest_id = %s
          AND start_date = %s
        """,
        [12, 2, "2026-08-01"],
    )

    assert rows == []