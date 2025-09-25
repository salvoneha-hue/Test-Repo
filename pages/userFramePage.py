import time
class UserFramePage:
    def __init__(self,page):
        self.page = page

    def emp_login(self,page):
        # Switch to iframe and click login
          self.frame = page.frame_locator("xpath=//iframe[@title='User: Immigration Employee Test User ~ Salesforce - Unlimited Edition']")
          login_button = self.frame.get_by_role("row", name="User Detail Edit Sharing").locator("input[name='login']")
          login_button.click()
          time.sleep(5)