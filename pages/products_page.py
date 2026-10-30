from playwright.sync_api import Page, expect

class orderProduct:
	def __init__(self, page: Page):
		self.page = page

		self.product = self.page.locator(".card-body").filter(has_text="ZARA COAT 3")
		self.add_to_cart = self.product.get_by_role("button", name="Add To Cart")
		self.cart_checkout_page = self.page.locator('button[routerlink="/dashboard/cart"]')



	def order(self):
		self.add_to_cart.click()
		self.cart_checkout_page.click()
		expect(self.page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/cart")
