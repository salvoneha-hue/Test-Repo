import time
class IXTFormPage:
    def __init__(self, page):
        self.page = page

    def fill_ixt_form(self,page):
         
         self. page.get_by_role("combobox", name="Requestor Type").click()
         self.page.get_by_text("Myself and/or dependent(s)").click()
         self.page.get_by_role("combobox", name="Category").click()
         self.page.get_by_text("Business International travel").click()
         self.page.get_by_role("combobox", name="Subcategory").click()
         self.page.get_by_text("General Global Visa Desk").click()
         self.page.get_by_role("combobox", name="Permiso Online Assessment").click()
         self.page.get_by_title("No", exact=True).click()
         self.page.get_by_role("combobox", name="Country of Travel").click()
         self.page.get_by_text("Afghanistan").click()
         self.page.get_by_role("combobox", name="Country of Travel 2").click()
         self.page.get_by_role("option", name="Argentina").click()
         self.page.get_by_role("combobox", name="Country of Travel 3").click()
         self.page.get_by_role("option", name="Australia").click()
         self.page.get_by_role("textbox", name="Upcoming Travel Start Date").click()
         self.page.get_by_label("-10-11").get_by_role("button", name="11").click()
         self.page.get_by_role("textbox", name="Upcoming Travel End Date").click()
         self.page.get_by_role("button", name="Next Month").click()
         self.page.get_by_role("button", name="13").click()
         self.page.locator(".slds-rich-text-area__content").click()
         self.page.get_by_role("textbox", name="Description").fill("Test")
         self.page.get_by_role("button", name="Submit").click()
         self.page.get_by_role("button", name="Yes").click()
         time.sleep(5)