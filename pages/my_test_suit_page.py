import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MyTestSuitPage(BasePage):

    def should_be_automated_filter(self):
        button_true = self.driver.find_element(By.ID, "filterByChange")
        button_true.click()

        button_prev = self.driver.find_element(By.LINK_TEXT, "Actual")

        button_auto = self.driver.find_element(By.LINK_TEXT, "Automated")
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", button_prev)
        button_auto.click()

        self.driver.find_element(By.CSS_SELECTOR, "[value='0']").click()

        button_ok = self.driver.find_element(By.ID, "filterCasesApply")
        button_ok.click()

        text = self.driver.find_element(By.ID, "groupsEmpty")
        welcome_text = text.text

        assert "No test cases found." == welcome_text
        button_remove = self.driver.find_element(By.ID, "filterCasesReset")

        button_remove.click()
        time.sleep(1)

        text_rem = self.driver.find_element(By.ID, "filterByEmpty")

        remove_text = text_rem.text

        assert "None" == remove_text

        self.driver.quit()

    def should_be_my_test_suit_page(self):
        self.driver.current_url

    def should_be_navigator_visible(self):
        text_nav = self.driver.find_element(By.ID, "navigation-project")
        navigator_text = text_nav.text

        assert "Стажировка 2022 Group 2" == navigator_text

    def should_visible_automated(self):
        self.driver.find_element(By.ID, "selectColumns-global").click()

        self.driver.find_element(By.ID, "selectColumnsAdd").click()

        self.driver.find_element(By.ID, "addColumnItems").click()

        button_add_automated = self.driver.find_element(By.ID, "addColumn-cases:custom_automation_type")
        button_add_automated.click()

        self.driver.find_element(By.ID, "addColumnSubmit").click()

        width_column = self.driver.find_element(By.ID, "columnWidth-cases:custom_automation_type")
        width_column.clear()
        width_column.click()

        width_column.send_keys('125')
        self.driver.find_element(By.ID, "selectColumnsSubmit").click()

        value_width = self.driver.find_element(By.CSS_SELECTOR, "[title='Automated']")

        text_value_width = value_width.text

        assert "Automated" == text_value_width

        self.driver.quit()

    def runs_should_be_more_than_one(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
        self.driver.find_element(By.ID, "navigation-suites").click()

        my_name = self.driver.find_element(By.ID, "suite-1064")
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", my_name)

        count_runs = self.driver.find_element(By.CSS_SELECTOR, "#suite-1064 .summary-description strong")

        text_value_width = count_runs.text
        count_runs_int = int(text_value_width)

        assert 1 < count_runs_int

        self.driver.quit()

    def true_in_automated(self):
        button_true = self.driver.find_element(By.ID, "filterByChange")
        button_true.click()
        conditions_of_use = self.driver.find_element(By.LINK_TEXT, "Automated")
        conditions_of_use.click()

    def on_checkbox_than_off(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

        prev_section = self.driver.find_element(By.ID, "sectionName-28449")
        self.driver.find_element(By.ID, "sectionName-28391")
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", prev_section)

        self.driver.find_element(By.CSS_SELECTOR, "#grid-28391 .checkbox .selectionCheckbox").click()
        count = self.driver.find_element(By.ID, "sectionCount-28391")
        count_text = count.text
        count_int = int(count_text)

        elements_1 = self.driver.find_elements(By.CSS_SELECTOR, "#grid-28391 .oddSelected")
        elements_2 = self.driver.find_elements(By.CSS_SELECTOR, "#grid-28391 .evenSelected")
        sum_elements = len(elements_1) + len(elements_2)
        time.sleep(1)
        assert count_int == sum_elements

        self.driver.find_element(By.CSS_SELECTOR, "#grid-28391 .checkbox .selectionCheckbox").click()

        elements_off = self.driver.find_elements(By.CSS_SELECTOR, "#grid-28391 .oddSelected")
        elements_off_2 = self.driver.find_elements(By.CSS_SELECTOR, "#grid-28391 .evenSelected")
        sum_elements_off = len(elements_off) + len(elements_off_2)
        assert 0 == sum_elements_off

        self.driver.quit()
