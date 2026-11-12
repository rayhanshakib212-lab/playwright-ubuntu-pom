from playwright.sync_api import Playwright


def test_update_product(playwright: Playwright):
    payload = {
    "title": "Samsung Galaxy S26",
    "price": 999
        }
    api_context = playwright.request.new_context(base_url = "https://dummyjson.com")
    response = api_context.put("/products/1", data = payload)

    assert response.status == 200
    body = response.json()
    assert body["id"] == 1
    assert body["title"] == payload["title"]
    assert body["price"] == payload["price"]
    print(f"the product title is {body["title"]}" f"\nand the price is {body["price"]}")
    api_context.dispose()



def test_patch_product(playwright: Playwright):
    payload = {
        "price": 799,
         }
    
    api_context = playwright.request.new_context(base_url = "https://dummyjson.com")
    response = api_context.patch("/products/1", data = payload)
    assert response.status == 200
    body = response.json()
    assert body["id"] == 1
    assert payload["price"] == body["price"]
    print(f"this is the new price{body["price"]}")
    api_context.dispose()




def test_delete_product(playwright: Playwright):
    api_context = playwright.request.new_context(base_url = "https://dummyjson.com")
    response = api_context.delete("/products/1")
    assert response.status == 200
    body = response.json()
    assert body["id"] == 1
    assert body["isDeleted"] is True
    print(body["id"])
    api_context.dispose()
