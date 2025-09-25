import re
import time

class ConfirmationPage:
    def __init__(self, page):
        self.page = page

    def get_ixt_id(self,page):
        confirmation_text = self.page.locator("body").inner_text()
        match = re.search(r"IXT-\d{8}", confirmation_text)
        record_id = match.group(0)
        return record_id
              