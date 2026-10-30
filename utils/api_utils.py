from urllib import response
from playwright.sync_api import Playwright

email = "smarthq@gmail.com"
password = "Imhere123!"


class APIUtils:


	def getToken(self,playwright: Playwright):
		api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
		response = api_request.post("https://rahulshettyacademy.com/api/ecom/auth/login",
					 data = {"userEmail": email, "userPassword": password})
		assert response.ok
		print(response.json())
		responseBody = response.json()
		return responseBody["token"]
