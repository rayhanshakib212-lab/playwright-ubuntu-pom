from playwright.sync_api import Playwright, Page
from pages.login_page import LoginPage
from pages.products_page import orderProduct
from pages.cart_page import cartPage
from pages.checkout_page import checkoutpage


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
