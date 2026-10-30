import time
from playwright.sync_api import expect, Playwright

def test_online_addtocart(playwright:Playwright):

	browser =  playwright.chromium.launch(headless=False)
	context =  browser.new_context()
	page = context.new_page()

	page.goto("https://rahulshettyacademy.com/client/#/auth/login")
	page.get_by_placeholder("email@example.com").fill("smarthq@gmail.com")
	page.get_by_placeholder("enter your passsword").fill("Imhere123!")
	page.locator("#login").click()



###############################################################################################################


	product = page.locator(".card-body").filter(has_text="ZARA COAT 3")
	product.get_by_role("button", name="Add To Cart").click()
	page.locator('button[routerlink="/dashboard/cart"]').click()
	expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/cart")


###############################################################################################################


	productdetailscart = page.locator("div[class='cartSection']").text_content()
	assert "ZARA COAT 3" in productdetailscart 
	#expect(productdetailscart).to_contain_text("ZARA COAT 3")
	#expect(productdetailscart).to_have_text("ZARA COAT 3")
	page.get_by_role("button", name="Checkout").click()

###############################################################################################################


	credit_card = page.get_by_text("Credit Card Number").locator("..").locator("input")
	credit_card.fill("4542 9931 9292 2293")
	CVVCode = page.get_by_text("CVV Code").locator("..").locator("input")
	CVVCode.fill("347")

	nameoncard = page.get_by_text("Name on Card").locator("..").locator("input")
	nameoncard.fill("Rayhan Shakib")

	page.get_by_placeholder("Select Country").type("ind")
	page.get_by_placeholder("Select Country").press("Enter")
	page.get_by_role("button", name="India").nth(1).click()
	page.get_by_text("Place Order").click()


###############################################################################################################

	time.sleep(10)

	expect(page.get_by_text("Thankyou for the order.")).to_have_text("Thankyou for the order.")
	
