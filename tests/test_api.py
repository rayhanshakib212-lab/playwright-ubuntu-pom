from playwright.sync_api import Playwright


# body = [
#     {"id": 1, "name": "Leanne", "email": "leanne@test.com"},
#     {"id": 2, "name": "Ervin", "email": "ervin@test.com"},
#     {"id": 3, "name": "Clementine", "email": "clementine@test.com"}
# ]


def test_get_users(playwright:Playwright):

    api_request = playwright.request.new_context(base_url = "https://jsonplaceholder.typicode.com")
    response = api_request.get("/users")

    assert response.status == 200

    body = response.json()

    #print(body)

    api_request.dispose()


    assert isinstance(body,list)
    assert len(body) == 10
    for user in body:     # doing a loop through each user
        assert "id" in user
        assert "name" in user
        assert "email" in user


    for user in body:
        assert isinstance(user["id"], int)
        assert user["id"] > 0
        assert isinstance(user["name"], str)
        assert "@" in user["email"]

    for user in body:
        if user["id"] == 3:
            assert user["name"] == "Clementine Bauch"
            cle = user["name"]

    print(cle)



    found = False

    for user in body:
        if user["id"] == 3:
            found = True
            assert user["name"] == "Clementine Bauch"
            break

    assert found, "User with ID 3 was not found"






def test_validate_stock_orders():
    body = {
        "orders": [
            {
            "symbol": "AAPL",
            "price": 250,
            "quantity": 10,
            "status": "FILLED",
            "order_total": 2500
        },
        {
            "symbol": "TSLA",
            "price": 400,
            "quantity": 5,
            "status": "PENDING",
            "order_total": 2000
        },
        {
            "symbol": "MSFT",
            "price": 500,
            "quantity": 3,
            "status": "FILLED",
            "order_total": 1500
        }
        ]
    }

    filled_symbols = []

    for order in body["orders"]:
        if order["status"] == "FILLED":
            filled_symbols.append(order["symbol"])

    assert filled_symbols == ["AAPL", "MSFT"]



    for order in body["orders"]:
        calculated_total = order["price"] * order["quantity"]

        assert calculated_total == order["order_total"]

        print(f'{order["symbol"]}: Total validated ${calculated_total}')




