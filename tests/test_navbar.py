from playwright.sync_api import Page, expect


def test_navigation_bar_contains_all_main_links(
    page: Page,
    web_client,
):
    response = web_client.get("/users/login")

    assert response.status_code == 200

    page.set_content(
        response.data.decode("utf-8"),
        wait_until="load",
    )

    expect(
        page.get_by_role("link", name="Home")
    ).to_have_attribute("href", "/")

    expect(
        page.get_by_role("link", name="Listings")
    ).to_have_attribute("href", "/listings")

    expect(
        page.get_by_role("link", name="Login")
    ).to_have_attribute("href", "/users/login")

    expect(
        page.get_by_role("link", name="Sign Up")
    ).to_have_attribute("href", "/users/new")