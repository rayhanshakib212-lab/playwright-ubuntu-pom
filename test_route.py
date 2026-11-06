from playwright.sync_api import Page



def test_route_fulfill(page: Page):

    def mock_response(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"userId": 1, "id": 101, "title": "Mock Order"}'
        )

    page.route("**/todos/1", mock_response)

    page.goto("https://jsonplaceholder.typicode.com/todos/1")

    assert page.locator("body").inner_text() == (
        '{"userId": 1, "id": 101, "title": "Mock Order"}'
    )
























# def test_mock_orders(page: Page):

#     def mock_response(route):
#         route.fulfill(
#             status=200,
#             content_type="application/json",
#             body='{"orders": [{"symbol": "AAPL", "quantity": 10}]}'

#         )

#     page.route("/api/orders", mock_response)

#     page.goto("https://example.com")



         