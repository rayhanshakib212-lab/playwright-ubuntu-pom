from playwright.sync_api import Playwright


def test_product(playwright: Playwright):
    api_context = playwright.request.new_context(base_url="https://dummyjson.com")
    response = api_context.get("/products/1")

    assert response.status() == 200
    body = response.json()
    print(body)
    assert body["id"] == 1
    assert body["price"] > 0
    assert len(body["title"]) > 0
    print(f'the product {body["title"]}' f'and the price is {body["price"]}')



def test_search_product(playwright: Playwright):
    product_ids = []
    api_context = playwright.request.new_context(base_url = "https://dummyjson.com")
    response = api_context.get("/products/search",params={"q": "phone"})
    body = response.json()
    assert response.status == 200
    assert body["total"] > 0
    for product in body["products"]:
        assert product["price"] > 0
        assert len(product["title"]) > 0
        product_ids.append(product["id"])
        print(f"the product is {product["title"]} its price is {product["price"]}")

    print(product_ids)
    assert len(product_ids) == len(body["products"])


    api_context.dispose()




def test_create_post(playwright: Playwright):
    api_context = playwright.request.new_context(base_url = "https://dummyjson.com")
    payload = {
    "title": "API Automation Practice",
    "body": "Testing POST requests using Playwright",
    "userId": 1}


    response = api_context.post("/posts/add", data = payload)

    assert response.status == 201
    body = response.json()

    assert body["title"] == "API Automation Practice"
    assert body["body"] == "Testing POST requests using Playwright"
    assert body["userId"] == 1

    assert body["id"] > 0
    assert "id" in body
    print(body["id"])

    api_context.dispose()
    





