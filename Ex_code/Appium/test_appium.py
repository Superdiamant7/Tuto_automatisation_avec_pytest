from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

def setup_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Device"
    options.app_package = "com.sec.android.app.popupcalculator"
    options.app_activity = "com.sec.android.app.popupcalculator.Calculator"
    options.no_reset = True

    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver

def test_addition():
    driver = setup_driver()

    try:
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="2"]').click()
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Plus"]').click()
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="3"]').click()
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Calcul"]').click()

        time.sleep(1)

        result_element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.sec.android.app.popupcalculator:id/calc_edt_formula"]')
        result = result_element.text.strip()

        assert "5" in result
        print("Test réussi !")
    
    finally:
        driver.quit()