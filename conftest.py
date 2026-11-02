from playwright.sync_api import Playwright
from utils.api_utils import APIUtils
import pytest
import allure


@pytest.fixture
def login_token(playwright):
    api = APIUtils()
    return api.getToken(playwright)




@pytest.fixture
def logged_in_page(page, login_token):
    page.console_logs = []

    page.on(
        "console",
        lambda msg: page.console_logs.append(msg.text)
    )

    page.add_init_script(
        f"""localStorage.setItem('token', '{login_token}')"""

    )

    page.goto("https://rahulshettyacademy.com/client")

    return page



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    is_xfail = report.skipped and hasattr(report, "wasxfail")

    if report.when == "call" and (report.failed or is_xfail):

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
            
            if hasattr(page, "console_logs"):
                allure.attach(
                    "\n".join(page.console_logs),
                    name="Browser Console Logs",
                    attachment_type=allure.attachment_type.TEXT
                )








def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Browser: chromium, firefox, or webkit"
    )


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser_name")





@pytest.fixture
def page(playwright, request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=True)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()

    page.console_logs = []

    page.on(
        "console",
        lambda msg: page.console_logs.append(msg.text)
    )

    yield page

    context.close()
    browser.close()



def pytest_configure(config):
    config.option.tracing = "on"
    config.option.reruns = 2
    config.option.reruns_delay = 1
    config.option.numprocesses = 2
