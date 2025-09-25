from playwright.sync_api import Page,expect
import time
import re

class RecordTypeValidationPage:
    def __init__(self, page):
        self.page = page

    def record_type_validation(self,page):
        
        expect(self.page.get_by_text("GVD – US Outbound Record", exact=True)).to_be_visible()
        return
    
    
    
        