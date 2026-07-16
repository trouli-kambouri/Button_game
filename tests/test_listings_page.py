from lib.database_connection import DatabaseConnection


SEED_FILE = "seeds/setup_seed_tables.sql"


def use_test_database(monkeypatch):
    monkeypatch.setattr(
        DatabaseConnection,
        "DEV_DATABASE_NAME",
        DatabaseConnection.TEST_DATABASE_NAME,
    )


def test_property_page_displays_the_selected_listing(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    response = web_client.get(
        "/listings/1?year=2026&month=1"
    )

    html = response.data.decode("utf-8")

    assert response.status_code == 200
    assert "Rain-soaked shed on a mountain" in html
    assert "Greenfield" in html
    assert "71 per night" in html
    assert "Greenfield.png" in html
    assert "booking-calendar" in html
    assert "January 2026" in html
def test_different_listing_ids_display_different_properties(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    first_response = web_client.get(
        "/listings/1?year=2026&month=1"
    )
    second_response = web_client.get(
        "/listings/2?year=2026&month=1"
    )

    assert b"Rain-soaked shed on a mountain" in first_response.data
    assert b"Uncomfortable camper van in a lay-by" not in (
        first_response.data
    )

    assert b"Uncomfortable camper van in a lay-by" in (
        second_response.data
    )
    assert b"Rain-soaked shed on a mountain" not in (
        second_response.data
    )


def test_property_page_contains_previous_and_next_month_links(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    response = web_client.get(
        "/listings/1?year=2026&month=1"
    )

    html = response.data.decode("utf-8")

    assert response.status_code == 200

    assert (
        "/listings/1?year=2025&month=12#booking-calendar"
        in html
    )

    assert (
        "/listings/1?year=2026&month=2#booking-calendar"
        in html
    )


def test_december_calendar_links_to_january_of_the_next_year(
    web_client,
    db_connection,
    monkeypatch,
):
    use_test_database(monkeypatch)
    db_connection.seed(SEED_FILE)

    response = web_client.get(
        "/listings/1?year=2026&month=12"
    )

    assert b"December 2026" in response.data
    assert (
        b"/listings/1?year=2027&month=1#booking-calendar"
        in response.data
    )
