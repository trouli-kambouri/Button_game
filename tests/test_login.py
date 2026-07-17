from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection


SEED_FILE = "seeds/setup_seed_tables.sql"


def use_test_database(monkeypatch):
    monkeypatch.setattr(
        DatabaseConnection,
        "DEV_DATABASE_NAME",
        DatabaseConnection.TEST_DATABASE_NAME
    )


def test_login_page_displays_form(
    page: Page,
    test_web_address: str
):
    page.goto(f"http://{test_web_address}/users/login")

    expect(
        page.get_by_role("heading", name="Login Page")
    ).to_be_visible()

    expect(page.locator('input[name="email"]')).to_be_visible()
    expect(page.locator('input[name="password"]')).to_be_visible()

    expect(
        page.locator('button[type="submit"]')
    ).to_be_visible()


def test_user_can_log_in(
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
        },
        follow_redirects=False
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/")


def test_wrong_password_redirects_to_login(
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
        },
        follow_redirects=False
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith(
        "/users/login"
    )


def test_unknown_email_redirects_to_login(
    web_client,
    db_connection,
    monkeypatch
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    response = web_client.post(
        "/sessions",
        data={
            "email": "unknown@example.com",
            "password": "password123"
        },
        follow_redirects=False
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith(
        "/users/login"
    )