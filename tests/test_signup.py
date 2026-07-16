from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection


SEED_FILE = "seeds/setup_seed_tables.sql"

#

def use_test_database(monkeypatch):
    monkeypatch.setattr(
        DatabaseConnection,
        "DEV_DATABASE_NAME",
        DatabaseConnection.TEST_DATABASE_NAME
    )


def test_signup_page_displays_form(
    page: Page,
    test_web_address: str
):
    page.goto(f"http://{test_web_address}/users/new")

    expect(
        page.get_by_role("heading", name="Sign Up Page")
    ).to_be_visible()

    expect(page.locator('input[name="name"]')).to_be_visible()
    expect(page.locator('input[name="password"]')).to_be_visible()
    expect(
        page.locator('input[name="phone_number"]')
    ).to_be_visible()
    expect(page.locator('input[name="email"]')).to_be_visible()

    expect(
        page.get_by_role("button", name="Sign Up")
    ).to_be_visible()


def test_user_can_sign_up(
    web_client,
    db_connection,
    monkeypatch
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    response = web_client.post(
        "/users",
        data={
            "name": "Anton Edeh",
            "password": "password123",
            "phone_number": "07123456789",
            "email": "anton@example.com"
        },
        follow_redirects=False
    )

    assert response.status_code == 302
    assert response.headers["Location"].endswith(
        "users/login"
    )

    users = db_connection.execute(
        """
        SELECT *
        FROM users
        WHERE email = %s
        """,
        ["anton@example.com"]
    )

    assert len(users) == 1
    assert users[0]["name"] == "Anton Edeh"
    assert users[0]["email"] == "anton@example.com"
    assert users[0]["phone_number"] == "07123456789"
    assert users[0]["password"] == "password123"


def test_duplicate_email_displays_error(
    web_client,
    db_connection,
    monkeypatch
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    response = web_client.post(
        "/users",
        data={
            "name": "Another Kayleigh",
            "password": "another-password",
            "phone_number": "07000000000",
            "email": "kayleighk@kickabout.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert response.request.path == "/users/new"

    assert (
        b"Email already exists. Please log-in."
        in response.data
    )

    users = db_connection.execute(
        """
        SELECT *
        FROM users
        WHERE email = %s
        """,
        ["kayleighk@kickabout.com"]
    )

    assert len(users) == 1