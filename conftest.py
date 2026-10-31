from playwright.sync_api import Playwright
from utils.api_utils import APIUtils
import pytest

@pytest.fixture
def login_token(playwright):
	api = APIUtils()
	return api.getToken(playwright)




@pytest.fixture
def logged_in_page(playwright, login_token):
	browser = playwright.chromium.launch(headless=True)
	context = browser.new_context()
	page = context.new_page()

	page.add_init_script(
		f"""localStorage.setItem('token', '{login_token}')"""

	)

	page.goto("https://rahulshettyacademy.com/client")

	return page
