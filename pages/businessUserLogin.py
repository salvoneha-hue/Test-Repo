import time
import re
class BusinessUserLoginPage:
    def __init__(self,page):
        self.page = page

    def business_user_login(self,page,testBusinessUser):   
       #  Search and select test business user
        time.sleep(3)
        search_box = self.page.get_by_role("combobox", name="Search Setup")
        search_box.click()
        search_box.fill(testBusinessUser)
        self.page.get_by_role("option", name="Immigration Test Business User1 User").click()

       # Login as the test business user
        self.frame = page.frame_locator("xpath=//iframe[@title='User: Immigration Test Business User1 ~ Salesforce - Unlimited Edition']")
        login_button = self.frame.get_by_role("row", name="User Detail Edit Sharing").locator("input[name='login']")
        login_button.click()




