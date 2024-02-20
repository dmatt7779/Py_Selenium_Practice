import pytest


@pytest.mark.usefixtures("driver")
class TestDummy():

    def test_dummy_func(self, driver):
        pass
        # driver.get("https://supersqa.com")
        # import pdb; pdb.set_trace()
