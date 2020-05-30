import pytest
from selenium import webdriver


class TestCase():
    @pytest.fixture()
    def test_setUp(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()
    
    def test_google(self, test_setUp):
        self.driver.get('https://www.google.com')
        assert 'google' in self.driver.title.lower()

        
