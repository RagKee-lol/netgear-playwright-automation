from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.wireless_page import WirelessPage
from config import SSID_NAME, SSID_PASSWORD
from utils.config import USERNAME, PASSWORD


def test_create_ssid(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    wireless = WirelessPage(page)

    login.open()
    login.login(USERNAME, PASSWORD)
    login.verify_login()

    dashboard.open_organization()
    dashboard.open_location()

    wireless.open()
    wireless.open_settings()
    wireless.add_ssid()
    wireless.create_ssid(SSID_NAME, SSID_PASSWORD,mode="NAT",band="2.4",security="WPA2 Personal Mixed")
    wireless.verify_ssid(SSID_NAME)
    
    
