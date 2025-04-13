from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# إعداد المتصفح (Chrome)
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

# ---------- TC01: التحقق من ظهور الفئات ----------
try:
    categories = driver.find_elements(By.XPATH, "//a[@class='list-group-item']")
    assert len(categories) >= 3
    print("TC01 Passed: الفئات ظاهرة.")
except Exception as e:
    print(f"TC01 Failed: {e}")

# ---------- TC02: التحقق من عرض تفاصيل المنتج ----------
try:
    first_product = driver.find_element(By.XPATH, "//div[@id='tbodyid']/div[1]/div/div/h4/a")
    product_name = first_product.text
    first_product.click()
    time.sleep(2)
    detail_title = driver.find_element(By.XPATH, "//h2[@class='name']").text
    assert product_name in detail_title
    print("TC02 Passed: تم عرض تفاصيل المنتج بشكل صحيح.")
    driver.back()
    time.sleep(2)
except Exception as e:
    print(f"TC02 Failed: {e}")

# ---------- TC03: التحقق من وظيفة البحث ----------
print("TC03 Skipped: لا يوجد شريط بحث حقيقي في موقع Demoblaze.")

# ---------- TC04: التحقق من التصفية حسب الفئة ----------
try:
    laptops_category = driver.find_element(By.LINK_TEXT, "Laptops")
    laptops_category.click()
    time.sleep(2)
    product_titles = driver.find_elements(By.XPATH, "//div[@id='tbodyid']/div/div/div/h4/a")
    assert all(p.is_displayed() for p in product_titles)
    print("TC04 Passed: تم عرض منتجات الحواسيب المحمولة بشكل صحيح.")
except Exception as e:
    print(f"TC04 Failed: {e}")

driver.quit()
