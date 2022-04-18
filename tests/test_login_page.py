from pages.login_page import LoginPage
from pages.my_test_suit_page import MyTestSuitPage


def test_successful_auth_to_my_test_suit_page(driver):
    link = "https://testrail.osinit.com/index.php?/auth/login/L3N1aXRlcy92aWV3LzEwNjQmZ3JvdXBfYnk9Y2FzZXM6c2VjdGlvbl9pZCZncm91cF9vcmRlcj1hc2MmZGlzcGxheV9kZWxldGVkX2Nhc2VzPTAmZ3JvdXBfaWQ9Mjg1OTAtOTc5NWRmNDI5YTIxNmNmMzE0NGJhZTVhOTBiOGU4MTFjZGY5YjYyMjg1MGM0MmYzNjM1MmYyMTgzMmQ5MmVkYQ::"
    page = LoginPage(driver, link)
    page.open()
    page.go_to_test_suit_page()
    my_test_suit_page = MyTestSuitPage(driver, driver.current_url)
    my_test_suit_page.should_be_my_test_suit_page()
    my_test_suit_page.should_be_navigator_visible()





