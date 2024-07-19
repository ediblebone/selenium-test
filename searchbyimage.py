from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def searchbyimage(visitResult, localPath, image, driver):
    screenshotPath = ''
    try:
        # open baidu page
        driver.get("https://www.baidu.com")

        # wait load search box
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "kw"))
        )

        # click search by image button
        camera_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='soutu-btn']"))
        )
        camera_icon.click()

        # upload image
        upload_input = driver.find_element(By.CSS_SELECTOR, "input.upload-pic")
        upload_input.send_keys(localPath + image + '.png')

        # wait the results
        time.sleep(5)
        results = driver.find_elements(By.XPATH, "//*[@class='general-imgcol-item']")

        # Check if the result index is valid
        if int(visitResult) > len(results) or int(visitResult) < 1:
            print(f"Result index is out of range.")
        else:
            # Visit the specified result
            result = results[int(visitResult) - 1]  # Indexing starts at 0
            result.click()

            # Wait for the result page to load
            time.sleep(5)  # Adjust based on your connection speed

            new_window_handle = driver.window_handles[-1]
            # switch to new window
            driver.switch_to.window(new_window_handle)
            # Take a screenshot of the visited page
            screenshotPath = localPath + image + '_shoot_' + visitResult + '.png'
            driver.save_screenshot(screenshotPath)
            time.sleep(1)
    finally:
        # close webpage
        driver.quit()

    return screenshotPath
