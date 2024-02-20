from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from ssqatest.driver.driver_manager import DriverManager


class FirefoxManager(DriverManager):
    def get_options(self):
        options = Options()
        options.accept_insecure_certs = True
        return options

    def get_driver(self):
        options = self.get_options()
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        return self.driver

