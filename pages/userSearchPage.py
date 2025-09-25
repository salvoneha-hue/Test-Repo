import time
class UserSearchPage:
    def __init__(self,page):
        self.page = page

    def emp_user_search(self,page,testEmpUser):
          time.sleep(3)
          self.page.get_by_role("button", name="Search").click()

    # Fill in the search box
          search_box = self.page.get_by_role("searchbox", name="Search...")
          search_box.fill(testEmpUser)
          search_box.press("Enter")
          

    # Open user details
          self.page.get_by_role("rowheader", name=testEmpUser).click()
          time.sleep(3)
          self.page.get_by_role("button", name="User Detail").click()
          time.sleep(15)


    


     
         