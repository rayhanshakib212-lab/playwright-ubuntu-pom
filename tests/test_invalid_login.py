from playwright.sync_api import expect


def test_invalid_login_displays_error(page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("invalid.user@example.com")
    page.get_by_placeholder("enter your passsword").fill("invalid-password")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Incorrect email or password.")).to_be_visible()
