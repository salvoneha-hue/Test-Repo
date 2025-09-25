import time
import re
from playwright.sync_api import Page,Playwright,sync_playwright,expect

class EmailSectionPage:
    def __init__(self, page):
        self.page = page

    def verify_email_status(self,page):
        self.page.get_by_role("link", name="View All Emails").click()
        self.page.get_by_role("link", name=re.compile(r"EMAIL-")).click()
        expect(self.page.locator("lightning-formatted-text").filter(has_text="Sent")).to_be_visible()