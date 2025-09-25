class CipAppPage:
    def __init__(self,page):
        self.page = page

    def open_cip_app(self):
        self.page.get_by_role("button", name="App Launcher").wait_for()
        self.page.get_by_role("button", name="App Launcher").click()
        self.page.get_by_role("combobox", name="Search apps and items...").wait_for()
        self.page.get_by_role("combobox", name="Search apps and items...").click()
        self.page.get_by_role("combobox", name="Search apps and items...").wait_for()
        self.page.get_by_role("combobox", name="Search apps and items...").fill("CIP")
        self.page.get_by_role("option", name="CIP").nth(1).wait_for()
        self.page.get_by_role("option", name="CIP").nth(1).click()
     