from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection


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


def test_signin_page_displays_form(
    page: Page,
    test_web_address: str
):
    page.goto(f"http://{test_web_address}/sessions/new")

    expect(
        page.get_by_role("heading", name="Sign in")
    ).to_be_visible()

    expect(page.locator('input[name="email"]')).to_be_visible()
    expect(
        page.locator('input[name="password"]')
    ).to_be_visible()

    expect(
        page.get_by_role("button", name="Sign in")
    ).to_be_visible()


def test_user_can_sign_in(
    page: Page,
    test_web_address: str,
    db_connection: DatabaseConnection
):
    create_test_user(db_connection)

    page.goto(f"http://{test_web_address}/sessions/new")

    page.locator('input[name="email"]').fill(
        "anton@example.com"
    )
    page.locator('input[name="password"]').fill(
        "password123"
    )

    page.get_by_role("button", name="Sign in").click()

    expect(page).to_have_url(
        f"http://{test_web_address}/"
    )


def test_user_cannot_sign_in_with_wrong_password(
    page: Page,
    test_web_address: str,
    db_connection: DatabaseConnection
):
    create_test_user(db_connection)

    page.goto(f"http://{test_web_address}/sessions/new")

    page.locator('input[name="email"]').fill(
        "anton@example.com"
    )
    page.locator('input[name="password"]').fill(
        "wrong-password"
    )

    page.get_by_role("button", name="Sign in").click()

    expect(
        page.get_by_text("Incorrect email or password")
    ).to_be_visible()

    expect(page).to_have_url(
        f"http://{test_web_address}/sessions/new"
    )