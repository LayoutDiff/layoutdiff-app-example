import argparse, sys
from appium import webdriver
from time import sleep

parser=argparse.ArgumentParser()

parser.add_argument('--apk-path', help='Path for apk file')
parser.add_argument('--device-name', help='Emulator name')
parser.add_argument('--screenshot-path', help='Path to save screenshots')

args=parser.parse_args()

# Add here the desired capabitilies described on appium desktop step
desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": args.device_name,
    "app": args.apk_path,
    "appPackage": "com.example.layoutdiffexample",
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2"
}

# Instantiating the appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def save_screenshot(screenshot_name):
    with open(f"{args.screenshot_path}/{screenshot_name}.png", "b") as file:
        file.write(driver.get_screenshot_as_base64())

driver.implicitly_wait(10)  # Set the amount of time the driver should wait when searching for elements (it's optional)

# Generated test script
save_screenshot("home_screen")
el1 = driver.find_element_by_accessibility_id("Press")
el1.click()
save_screenshot("home_screen_click_1")

sleep(1)
el1.click()
save_screenshot("home_screen_click_2")

sleep(1)
el1.click()
save_screenshot("home_screen_click_3")

sleep(1)
el1.click()
save_screenshot("home_screen_click_4")

sleep(1)
el1.click()
save_screenshot("home_screen_click_5")