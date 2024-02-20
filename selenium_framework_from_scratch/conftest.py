import pytest

from ssqatest.driver import driver_manager_factory


@pytest.fixture(scope="class")
def driver(request):
    browser = request.config.getoption("--browser")
    driver_manager = driver_manager_factory.get_manager(browser)
    yield driver_manager.get_driver()
    # driver_manager.remove_driver()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="Browser where the test will be executed",
                     choices=("chrome", "firefox"))
