import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from ssqatest.driver.driver_manager import DriverManager

log = logging.getLogger(__name__)


class ChromeManager(DriverManager):

    def get_options(self):
        options = Options()
        options.accept_insecure_certs = True
        return options

    def get_driver(self):
        options = self.get_options()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        return self.driver
