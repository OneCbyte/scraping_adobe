from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def conversion(url, file_path):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": r"your_location"
    })
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.get(url)
    browser.maximize_window()
    element = browser.find_element(By.XPATH, "//*[@class='FileUpload__fileInput___NKeOg']")
    element.send_keys(file_path)
    try:
        WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "//button[@class='Dniwja_spectrum-Button Dniwja_spectrum-BaseButton Dniwja_i18nFontFamily Dniwja_spectrum-FocusRing Dniwja_spectrum-FocusRing-ring Download__downloadButton___2qFEa']")))
        browser.find_element(By.XPATH, "//button[@class='Dniwja_spectrum-Button Dniwja_spectrum-BaseButton Dniwja_i18nFontFamily Dniwja_spectrum-FocusRing Dniwja_spectrum-FocusRing-ring Download__downloadButton___2qFEa']").click()
        time.sleep(10)
    except:
        print("Error!")
