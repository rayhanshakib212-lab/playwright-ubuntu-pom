from playwright.sync_api import Page

class LoginPage:

	def __init__(self, page:Page):
		self.page = page

		self.email = page.get_by_placeholder("email@example.com")
		self.password = page.get_by_placeholder("enter your passsword")
		self.login_button = page.locator("#login")



	def navigate(self):
		self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")


	def log(self, email, password):
		self.email.fill( email )
		self.password.fill( password )
		self.login_button.click()
