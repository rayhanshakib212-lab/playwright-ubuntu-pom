from playwright.sync_api import Page

class checkoutpage:
	def __init__(self, page: Page):
		self.page = page
		self.credit_card = self.page.get_by_text("Credit Card Number").locator("..").locator("input")
		self.CVVCode = self.page.get_by_text("CVV Code").locator("..").locator("input")
		self.nameoncard = self.page.get_by_text("Name on Card").locator("..").locator("input")
		self.country_dropdown =self.page.get_by_placeholder("Select Country")
		self.dropdown_option = self.page.get_by_role("button", name="India")
		self.placeorder_button = self.page.get_by_text("Place Order")


	def fillout_checkout(self):
		self.credit_card.fill("4542 9931 9292 2293")
		self.CVVCode.fill("347")
		self.nameoncard.fill("Rayhan Shakib")
		self.country_dropdown.type("ind")
		self.country_dropdown.press("Enter")
		self.dropdown_option.nth(1).click() # selecting second option 'india' from dropdown
		self.placeorder_button.click()
