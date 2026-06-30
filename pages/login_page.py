from utils.config import LOGIN_URL
from utils.logger import logger
class LoginPage:
	def __init__(self,page):
		self.page = page
	def open(self):
		logger.info("Opening Netgear Login")
		self.page.goto(LOGIN_URL)
	def enter_email(self,email):
		self.page.locator("input[type='email']").fill(email)
	def enter_password(self,password):
		self.page.locator("input[type='password']").fill(password)
	def click_login(self):
		self.page.get_by_role("button",name="Sign In").click()
	def login(self,email,password):
		self.enter_email(email)
		self.enter_password(password)
		self.click_login()
	def verify_login(self):
		self.page.wait_for_load_state("networkidle")
		assert "insight" in self.page.url.lower()
