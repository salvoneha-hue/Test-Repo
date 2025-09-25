from playwright.sync_api import Page
import time
import re
import pages.confirmationPage

class RecordDetailPage:
    def __init__(self, page):
        self.page = page

    def record_detail(self,record_id):
        time.sleep(5)
        self.page.get_by_role("button", name="Search").click()
        time.sleep(3)   
        search_input = self.page.get_by_role("searchbox", name="Search...")
        time.sleep(3)
        search_input.fill(record_id)
        search_input.press("Enter")
        self.page.get_by_role("link", name=re.compile(r"IXT-")).first.wait_for()
        self.page.get_by_role("link", name=re.compile(r"IXT-")).first.click()
        time.sleep(4)