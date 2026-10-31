from playwright.sync_api import Playwright
from utils.api_utils import APIUtils
import pytest
import allure


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



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("logged_in_page")

        if page is None:
            page = item.funcargs.get("page")
	if page:
	    screenshot = page.screenshot()

	    allure.attach(
	        screenshot,
	        name="Failure Screenshot",
	        attachment_type=allure.attachment_type.PNG
	    )

