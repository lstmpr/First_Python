from pages.login_page import LoginPage
from pages.my_test_suit_page import MyTestSuitPage

def test_on_checkbox_than_off(driver):
    link = "https://testrail.osinit.com/index.php?/auth/login" \
           "/L3N1aXRlcy92aWV3LzEwNjQmZ3JvdXBfYnk9Y2FzZXM6c2VjdGlvbl9pZCZncm91cF9vcmRlcj1hc2MmZGlzcGxheV9kZWxldGVkX2Nhc2VzPTAmZ3JvdXBfaWQ9Mjg1OTAtOTc5NWRmNDI5YTIxNmNmMzE0NGJhZTVhOTBiOGU4MTFjZGY5YjYyMjg1MGM0MmYzNjM1MmYyMTgzMmQ5MmVkYQ:: "
    page = LoginPage(driver, link)
    page.open()
    page.go_to_test_suit_page()
    page_testrail = MyTestSuitPage(driver, link)
    page_testrail.on_checkbox_than_off()
