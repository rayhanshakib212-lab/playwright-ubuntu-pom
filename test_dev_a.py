import sync_api from Playwright


def test_product(playwright: Playwright):
    api_context = playwright.request.new_context(base_url="https://dummyjson.com")
    response = api_context.get("/products/1")

    assert response.status() == 200
    body = response.json()
    print(body)
    assert product["id"] == 1
    assert product["price"] > 0
    assert len(product["title"]) > 0
    print(f'the product {product["title"]}' f'and the price is {product["price"]}')
