from abc import ABC, abstractmethod


class DriverManager(ABC):
    def __init__(self):
        self.driver = None

    @abstractmethod
    def get_driver(self):
        pass

    @abstractmethod
    def get_options(self):
        pass

    def remove_driver(self):
        self.driver.close()
        self.driver.quit()
