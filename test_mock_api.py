from playwright.sync_api import Page, Route


def test_mock_get_product(page: Page):
    mock_product = {
        "id": 1,
        "title": "Samsung Galaxy S26",
        "price": 799
    }


    def mock_response(route: Route):
        route.fulfill(
            status=200,
            json=mock_product
        )

    page.route(
        "**/products/1",
        mock_response
    )


    with page.expect_response("**/products/1") as response_info:
        page.goto("https://dummyjson.com/products/1")   

    response = response_info.value
    body = response.json()


    assert response.status == 200
    assert body["id"] == mock_product["id"]
    assert body["title"] == mock_product["title"]
    assert body["price"] == mock_product["price"]

    print(body)








def test_mock_get_user(page: Page):
    mock_user = {
    "id": 1,
    "firstName": "John",
    "lastName": "Smith",
    "age": 30,
    "email": "john@example.com"
    }


    def mock_response(route: Route):
        route.fulfill(
            status=200,
            json=mock_user
        )


    page.route("**/users/1", mock_response )


    with page.expect_response("**/users/1") as response_info:
        page.goto("https://dummyjson.com/users/1")

    response = response_info.value
    body = response.json()






def test_mock_get_cart(page: Page):


    mock_cart = {
    "id": 1,
    "userId": 5,
    "products": [
        {
            "id": 101,
            "title": "Laptop",
            "price": 800,
            "quantity": 2
        },
        {
            "id": 102,
            "title": "Mouse",
            "price": 25,
            "quantity": 1
        }
    ],
    "total": 1625
    }


    def mock_response(route: Route):
        route.fulfill(status=200, json=mock_cart)

    page.route("**/carts/1", mock_response)


    with page.expect_response("**/carts/1") as response_info:
        page.goto("https://dummyjson.com/carts/1")

    response = response_info.value
    body = response.json()
    # NOT COMPLETED HERE








def test_mock_404(page: Page):

    mock_error = {
        "message": "Product not found",
        "status": 404
    }


    def mock_response(route: Route):

        route.fulfill(
            status = 404,
            json=mock_error
        )



    page.route("**/products/999",mock_response)


    with page.expect_response("**/products/999") as response_info:
        page.goto("https://dummyjson.com/products/999")







def test_mock_user_404(page: Page):

    mock_error = {'message':"User not found",
    'status':404,
    'userId':999}

    def mock_response(route: Route):
        route.fulfill(
            status = 404,
            json = mock_error
        )

    page.route("**/users/999", mock_response)

    with page.expect_response("**/users/999") as response_info:
        page.goto("https://dummyjson.com/users/999")


    response = response_info.value
    body = response.json()

    assert response.status == 404
    assert body["message"] == "User not found"
    assert body["status"] == 404
    assert body["userId"] == 999

    # HTTP response status equals 404.
    # body["message"] equals "User not found".
    # body["status"] equals 404.
    # body["userId"] equals 999.


