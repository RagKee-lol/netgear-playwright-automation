from utils.logger import logger
from playwright.sync_api import expect

class WirelessPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        logger.info("Opening Wireless")
        self.page.get_by_role("link", name="Wireless").click()

    def open_settings(self):
        logger.info("Opening Wireless Settings")
        self.page.locator("#divLocBarwirquickView").get_by_role("link", name="Settings").click()

    def add_ssid(self):
        logger.info("Opening Add SSID")
        btn=self.page.locator("#ancssidModWirSett")
        btn.wait_for(state="visible")
        btn.scroll_into_view_if_needed()
        btn.click()
    def create_ssid(self,ssid,password,mode="Bridge",band="ALL",security="WPA2 Personal"):
    	logger.info("Creating SSID")
    	self.page.locator("#ssid").fill(ssid)
    	self.page.locator("#password").fill(password)
    	if mode=="NAT":
    		self.select_nat_mode()
    		ip=self.page.locator('input[name="ipAddress"]')
    		ip.wait_for(state="visible")
    		ip.scroll_into_view_if_needed()
    		ip.fill("172.31.3.1")
    	if band == "2.4":
    		self.set_band("2.4",True)
    		self.set_band("5",False)
    	elif band == "5":
    		self.set_band("2.4",False)
    		self.set_band("5",True)
    	self.set_security(security)
    	self.page.locator("#password").scroll_into_view_if_needed()
    	self.page.get_by_text("Save").nth(2).scroll_into_view_if_needed()
    	self.page.get_by_text("Save").nth(2).click()
    	if mode=="NAT":
    		self.confirm_nat_popup()
    	self.page.wait_for_timeout(5000)
    def verify_ssid(self,ssid_name):
    	logger.info(f"Verifying SSID:{ssid_name}")
    	expect(
    	self.page.get_by_text(ssid_name,exact=True)).to_be_visible(timeout=10000)
    def set_band(self, band, enable=True):
    	logger.info(f"{'Enabling' if enable else 'Disabling'} {band}")
    	if band == "2.4":
    		checkbox_id = "band_2"
    	elif band == "5":
    		checkbox_id= "band_5"
    	else:
    		raise ValueError(f"Invalid band: {band}")
    	checkbox = self.page.locator(f"#{checkbox_id}")
    	if checkbox.is_checked() != enable:
    		self.page.evaluate(f"document.getElementById('{checkbox_id}').click();")
    def set_security(self,security):
    	logger.info(f"Setting security to {security}")
    	if security=="Open":
    		value = "0"
    	elif security == "WPA2 Personal":
    		value = "32"
    	elif security == "WPA2 Personal Mixed":
    		value = "48"
    	elif security == "WPA3 Personal":
    		value = "80"
    	elif security == "WPA3 Personal Mixed":
    		value = "96"
    	elif security == "WPA3 Enterprise":
    		value="112"
    	else:
    		raise ValueError(f"Unknown security: {security}")
    	self.page.locator("#security").select_option(value=value)
    def select_nat_mode(self):
    	logger.info("Selecting NAT mode")
    	self.page.locator('select[name="trafficType"]').scroll_into_view_if_needed()
    	self.page.locator('select[name="trafficType"]').select_option("1")
    	return
    def confirm_nat_popup(self):
    	logger.info("Confirming NAT popup")
    	self.page.get_by_role("button", name="Yes, proceed").click()
    	return
   	
    
    	
    	
