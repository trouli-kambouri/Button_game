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


def sign_in(
    page: Page,
    test_web_address: str
):
    page.goto(f"http://{test_web_address}/sessions/new")

    page.locator('input[name="email"]').fill(
        "anton@example.com"
    )
    page.locator('input[name="password"]').fill(
        "password123"
    )

    page.get_by_role("button", name="Sign in").click()


def test_signed_out_user_cannot_access_new_listing_page(
    page: Page,
    test_web_address: str
):
    page.goto(f"http://{test_web_address}/listings/new")

    expect(page).to_have_url(
        f"http://{test_web_address}/sessions/new"
    )


def test_signed_in_user_can_access_new_listing_page(
    page: Page,
    test_web_address: str,
    db_connection: DatabaseConnection
):
    create_test_user(db_connection)
    sign_in(page, test_web_address)

    page.goto(f"http://{test_web_address}/listings/new")

    expect(page).to_have_url(
        f"http://{test_web_address}/listings/new"
    )

    expect(
        page.get_by_role(
            "heading",
            name="Create a new listing"
        )
    ).to_be_visible()