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


def test_successful_login_creates_session_cookie(
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

    expect(page).to_have_url(
        f"http://{test_web_address}/"
    )

    cookies = page.context.cookies()

    session_cookies = [
        cookie
        for cookie in cookies
        if cookie["name"] == "session"
    ]

    assert len(session_cookies) == 1


def test_failed_login_does_not_create_session_cookie(
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

    expect(page).to_have_url(
        f"http://{test_web_address}/users/login"
    )

    cookies = page.context.cookies()

    session_cookies = [
        cookie
        for cookie in cookies
        if cookie["name"] == "session"
    ]

    assert len(session_cookies) == 0