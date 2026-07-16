from lib.database_connection import DatabaseConnection


SEED_FILE = "seeds/setup_seed_tables.sql"


def use_test_database(monkeypatch):
    monkeypatch.setattr(
        DatabaseConnection,
        "DEV_DATABASE_NAME",
        DatabaseConnection.TEST_DATABASE_NAME
    )


def test_successful_login_creates_session(
    web_client,
    db_connection,
    monkeypatch
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    response = web_client.post(
        "/sessions",
        data={
            "email": "kayleighk@kickabout.com",
            "password": "badpassword"
        }
    )

    assert response.status_code == 302

    with web_client.session_transaction() as flask_session:
        assert flask_session["user_id"] == 1
        assert (
            flask_session["email"]
            == "kayleighk@kickabout.com"
        )


def test_failed_login_does_not_create_session(
    web_client,
    db_connection,
    monkeypatch
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    response = web_client.post(
        "/sessions",
        data={
            "email": "kayleighk@kickabout.com",
            "password": "wrong-password"
        }
    )

    assert response.status_code == 302

    with web_client.session_transaction() as flask_session:
        assert "user_id" not in flask_session
        assert "email" not in flask_session