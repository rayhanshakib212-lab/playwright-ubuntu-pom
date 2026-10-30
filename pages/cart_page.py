from playwright.sync_api import Page

class cartPage:
	def __init__(self, page:Page):
		self.page = page
		self.productdetailscart = self.page.locator("div[class='cartSection']")
		self.checkout_button = self.page.get_by_role("button", name="Checkout")


	def confirm_cart(self):
		self.productdetailscart_contains = self.productdetailscart.text_content()
		assert "ZARA COAT 3" in self.productdetailscart_contains
		self.checkout_button.click()
