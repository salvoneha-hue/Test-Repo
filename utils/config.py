import os
from dotenv import load_dotenv
 
load_dotenv()
 
BASE_URL = os.getenv("base_url")
USERNAME = os.getenv("user")
PASSWORD = os.getenv("password")
TEST_EMP_USER = os.getenv("test_emp_user")
TEST_BUSINESS_USER = os.getenv("test_business_user")