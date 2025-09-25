class LoginPage:
    def __init__(self,page):
        self.page = page


    def navigate(self,baseUrl):
        self.page.goto(baseUrl)

    def login(self,userName,userPassword):
         self.page.locator("input[name='username']").fill(userName)
         self.page.locator("input[name='pw']").fill(userPassword)
         self.page.locator("#rememberUn").check()
         self.page.get_by_role("button", name="Log In to Sandbox").click()
         