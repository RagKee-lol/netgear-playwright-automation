from utils.logger import logger

class DashboardPage:

    def __init__(self, page):
        self.page = page

    def open_organization(self):
        logger.info("Opening Organization")
        self.page.get_by_text("Zilogic Systems").nth(1).click()

    def open_location(self):
        logger.info("Opening Location")
        admin=self.page.locator('[id="_divMainOrg"]').get_by_text("admin")
        admin.wait_for(state='visible')
        admin.scroll_into_view_if_needed()
        admin.click(force=True)
        self.page.wait_for_load_state("networkidle")
        
