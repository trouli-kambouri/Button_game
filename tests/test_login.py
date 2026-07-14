from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection


def reset_database(db_connection: DatabaseConnection):
    db_connection.execute(
        """
        TRUNCATE TABLE listings, users
        RESTART IDENTITY CASCADE
        """
    )


def create_test_user(
    db_connection: DatabaseConnection
):
    db_connection.execute(
        """
        INSERT INTO users
            (name, email, phone_number, password)
        VALUES
            (%s, %s, %s, %s)
        """,
        [
            "Anton Edeh",
            "anton@example.com",
            "07123456789",
            "password123"
        ]
    )


def test_login_page_displays_form(
    page: Page,
    test_web_address: str,
    db_connection: DatabaseConnection
):
    reset_database(db_connection)

    page.goto(f"http://{test_web_address}/users/login")

    expect(page.locator('input[name="email"]')).to_be_visible()
    expect(page.locator('input[name="password"]')).to_be_visible()

    expect(
        page.locator(
            'button[type="submit"], input[type="submit"]'
        )
    ).to_be_visible()


def test_user_can_log_in(
    page: Page,
    test_web_address: str,
    db_connection: DatabaseConnection
):
    reset_database(db_connection)
    create_test_user(db_connection)

    page.goto(f"http://{test_web_address}/users/login")

    page.locator('input[name="email"]').fill(
        "anton@example.com"
    )
    page.locator('input[name="password"]').fill(
        "password123"
    )

    page.locator(
        'button[type="submit"], input[type="submit"]'
    ).click()

    # Successful login redirects to the landing page
    expect(page).to_have_url(
        f"http://{test_web_address}/"
    )


def test_user_cannot_log_in_with_wrong_password(
    page: Page,
    test_web_address: str,
    db_connection: DatabaseConnection
):
    reset_database(db_connection)
    create_test_user(db_connection)

    page.goto(f"http://{test_web_address}/users/login")

    page.locator('input[name="email"]').fill(
        "anton@example.com"
    )
    page.locator('input[name="password"]').fill(
        "wrong-password"
    )

    page.locator(
        'button[type="submit"], input[type="submit"]'
    ).click()

    # app.py redirects failed logins back to the login page
    expect(page).to_have_url(
        f"http://{test_web_address}/users/login"
    )