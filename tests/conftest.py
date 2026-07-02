import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DRIVER_PATH = os.path.join(ROOT_DIR, "drivers", "geckodriver.exe")
BASE_URL = "https://qa-scooter.praktikum-services.ru/"  


@pytest.fixture(scope="function")
def driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--width=1280")
    firefox_options.add_argument("--height=1024")

    service = FirefoxService(executable_path=DRIVER_PATH)
    driver = webdriver.Firefox(service=service, options=firefox_options)
    
    driver.get(BASE_URL)  
    yield driver
    
    driver.quit()