
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoblazeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_TC01_verify_categories_visible(self):
        categories = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='list-group-item']")))
        self.assertGreaterEqual(len(categories), 3)
        print("TC01 Passed: الفئات ظاهرة.")

    def test_TC02_verify_product_details_display(self):
        first_product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='tbodyid']/div[1]/div/div/h4/a")))
        product_name = first_product.text
        first_product.click()
        detail_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='name']"))).text
        self.assertIn(product_name, detail_title)
        print("TC02 Passed: تم عرض تفاصيل المنتج بشكل صحيح.")
        self.driver.back()

    def test_TC03_no_search_bar(self):
        print("TC03 Skipped: لا يوجد شريط بحث حقيقي في موقع Demoblaze.")

    def test_TC04_verify_filter_by_category_laptops(self):
        laptops_category = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops")))
        laptops_category.click()
        product_titles = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='tbodyid']/div/div/div/h4/a")))
        for p in product_titles:
            self.assertTrue(p.is_displayed())
        print("TC04 Passed: تم عرض منتجات الحواسيب المحمولة بشكل صحيح.")

if __name__ == "__main__":
    unittest.main()
