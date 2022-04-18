import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    #print("\nstart browser for test..")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.implicitly_wait(3)
    driver.maximize_window()
    # #print("\nquit browser..")
    # driver.quit()