from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection


def test_signup_page_displays_form(
    page: Page,
    test_web_address: str
):
    page.goto(f"http://{test_web_address}/users/new")

    expect(
        page.get_by_role("heading", name="Sign up")
    ).to_be_visible()

    expect(page.locator('input[name="name"]')).to_be_visible()
    expect(page.locator('input[name="email"]')).to_be_visible()
    expect(
        page.locator('input[name="phone_number"]')
    ).to_be_visible()
    expect(page.locator('input[name="password"]')).to_be_visible()

    expect(
        page.get_by_role("button", name="Sign up")
    ).to_be_visible()


def test_user_can_sign_up(
    page: Page,
    test_web_address: str,
    db_connection: DatabaseConnection
):
    page.goto(f"http://{test_web_address}/users/new")

    page.locator('input[name="name"]').fill("Anton Edeh")
    page.locator('input[name="email"]').fill(
        "anton@example.com"
    )
    page.locator('input[name="phone_number"]').fill(
        "07123456789"
    )
    page.locator('input[name="password"]').fill(
        "password123"
    )

    page.get_by_role("button", name="Sign up").click()

    expect(page).to_have_url(
        f"http://{test_web_address}/sessions/new"
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