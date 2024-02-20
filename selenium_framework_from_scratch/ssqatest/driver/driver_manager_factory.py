import logging

from ssqatest.driver.browser_managers.chrome_manager import ChromeManager
from ssqatest.driver.browser_managers.firefox_manager import FirefoxManager

log = logging.getLogger(__name__)


def get_manager(browser):
    match browser:
        case "chrome":
            log.info("Using Chrome browser")
            manager = ChromeManager()
        case "firefox":
            log.info("Using Firefox browser")
            manager = FirefoxManager()
        case _:
            log.warning("No browser provided by command line, using Chrome browser as default")
            manager = ChromeManager()

    return manager
