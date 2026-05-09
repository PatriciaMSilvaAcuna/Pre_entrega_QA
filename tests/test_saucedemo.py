from utils.helpers import login

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login( driver ):
    login(driver, "standard_user", "secret_sauce")