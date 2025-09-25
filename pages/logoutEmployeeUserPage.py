import time
class LogoutEmployeeUserPage:
    def __init__(self, page):
        self.page = page

    def logout_user(self,page):
        self.page.goto("https://deloitteimmigration--qa.sandbox.lightning.force.com/lightning/page/home")
        self.page.get_by_role("link", name="Log out as Immigration").click()