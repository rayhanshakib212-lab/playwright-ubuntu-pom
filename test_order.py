from playwright.sync_api import Playwright, Page, expect
from pages.login_page import LoginPage
from pages.products_page import orderProduct
from pages.cart_page import cartPage
from pages.checkout_page import checkoutpage
from utils.api_utils import APIUtils
import pytest
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




def test_api_get_token(logged_in_page):

	#api_calls =  APIUtils()
	#Token =	api_calls.getToken(playwright) no longer needed, we move it to the fixture login_token
	#browser = playwright.chromium.launch(headless=True)
	#context = browser.new_context()
	#page = context.new_page()
	#page.add_init_script(f"""localStorage.setItem('token', '{login_token}')""")
	#page.goto("https://rahulshettyacademy.com/client")**we wont need this because of 'logged_in_page' fixture**
	logged_in_page.get_by_role("button", name="ORDERS").click()
	expect(logged_in_page.get_by_text('Your Orders')).to_be_visible()




@pytest.mark.xfail(reason="Intentinal failure to test screenshot capture")
def test_for_screenshots(logged_in_page):
	logged_in_page.get_by_role("button", name="ORDERS").click()
	expect(logged_in_page.get_by_text('Your rders')).to_be_visible() # will fail here

