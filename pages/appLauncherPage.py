
import time
class AppLauncherPage:
    def __init__(self, page):
        self.page = page

    def open_ixt_webform(self,page):
         self.page.get_by_role("button", name="App Launcher").click()
         search_combobox = self.page.get_by_role("combobox", name="Search apps and items...")
         search_combobox.click()
         search_combobox.fill("ixt")
         self.page.get_by_role("option", name="IXT Mailbox WebForm").click()
         time.sleep(5)