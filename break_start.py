from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Set up Chrome options to connect to the debugging instance
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "127.0.0.1:9222"

# Connect to the existing Chrome instance
driver = webdriver.Chrome(options=chrome_options)

# Open a new tab using JavaScript
driver.execute_script("window.open('', '_blank');")

# Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[-1])

# Navigate to the page with the button in the new tab
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfB_Rgk8aTVc48vkML9opzeHoYrqqVs8-wr0DVcR0myNLSKhg/viewform")

# Define a WebDriverWait with a timeout
wait = WebDriverWait(driver, 10)

time.sleep(1)

aria_checked1 = driver.execute_script('return document.getElementById("i5").getAttribute("aria-checked");')
aria_checked2 = driver.execute_script('return document.getElementById("i12").getAttribute("aria-checked");')
aria_checked3 = driver.execute_script('return document.getElementById("i46").getAttribute("aria-checked");')

if aria_checked1 == "true":
    print("The checkbox 1 is already checked. No need to check.")
else:
    # Wait for the checkbox to be clickable
    checkbox1 = wait.until(EC.element_to_be_clickable((By.ID, "i5")))
    # Move the mouse away from the interfering element
    ActionChains(driver).move_to_element(checkbox1).perform()
    checkbox1.click()
    print("The checkbox 1 is not checked. Checking the checkbox.")

if aria_checked2 == "true":
    print("The checkbox 2 is already checked. No need to check.")
else:
    checkbox2 = wait.until(EC.element_to_be_clickable((By.ID, "i12")))
    ActionChains(driver).move_to_element(checkbox2).perform()
    checkbox2.click()
    print("The checkbox 2 is not checked. Checking the checkbox.")

if aria_checked3 == "true":
    print("The checkbox 3 is already checked. No need to check.")
else:
    checkbox3 = wait.until(EC.element_to_be_clickable((By.ID, "i46")))
    ActionChains(driver).move_to_element(checkbox3).perform()
    checkbox3.click()
    print("The checkbox 3 is not checked. Checking the checkbox.")

# Wait for the input element by XPath
input_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@class="Hvn9fb zHQkBf"]')))
value = input_element.get_attribute('value')

if value == '':
    print("Input text field is empty.")
    input_element.send_keys("569")
else:
    print("Text field contains texts. Clearing out the texts")
    input_element.clear()
    input_element.send_keys("569")

# Click "Next" button
print("Clicking Next")
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@jsname="OCpkoe"]')))
ActionChains(driver).move_to_element(next_button).perform()
next_button.click()


time.sleep(1)
# Check if the checkbox 4 is already checked. (CHECKOUT ID i11)
aria_checked4 = driver.execute_script('return document.getElementById("i11").getAttribute("aria-checked");')

if aria_checked4 == "true":
    print("The checkbox 4 is already checked. No need to check.")
else:
    checkbox4 = wait.until(EC.element_to_be_clickable((By.ID, "i11")))
    ActionChains(driver).move_to_element(checkbox4).perform()
    checkbox4.click()
    print("The checkbox 4 is not checked. Checking the checkbox.")

# Wait for the "Submit" button
# submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@jsname="M2UYVd"]')))
# ActionChains(driver).move_to_element(submit_button).perform()
# submit_button.click()

print("Check-In Submitted")

# Switch tab
driver.switch_to.window(driver.window_handles[-1])

# Optionally, you can close the browser or the new tab
# driver.quit()  # Close the entire browser
# driver.close()  # Close the current tab
