from playwright.sync_api import Playwright, Page, expect
from pages.login_page import LoginPage
from pages.products_page import orderProduct
from pages.cart_page import cartPage
from pages.checkout_page import checkoutpage
from utils.api_utils import APIUtils

def test_e2e_order(page:Page):


	loginpage =  LoginPage(page)
	products = orderProduct(page)
	cart = cartPage(page)
	checkout = checkoutpage(page)

	loginpage.navigate()
	loginpage.log('smarthq@gmail.com','Imhere123!')

	products.order()

	cart.confirm_cart()

	checkout.fillout_checkout()




def test_api_get_token(playwright:Playwright):

	api_calls =  APIUtils()
	Token =	api_calls.getToken(playwright)
	browser = playwright.chromium.launch(headless=True)
	context = browser.new_context()
	page = context.new_page()
	page.add_init_script(f"""localStorage.setItem('token', '{Token}')""")
	page.goto("https://rahulshettyacademy.com/client")
	page.get_by_role("button", name="ORDERS").click()
	expect(page.get_by_text('Your Orders')).to_be_visible()

