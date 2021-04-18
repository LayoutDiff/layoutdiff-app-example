import argparse, sys
from appium import webdriver
from time import sleep

parser=argparse.ArgumentParser()

parser.add_argument('--apk-path', help='Path for apk file')
parser.add_argument('--device-name', help='Emulator name')

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

print(desired_caps)

# Instantiating the appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # Set the amount of time the driver should wait when searching for elements (it's optional)

# Generated test script

background_color = driver.find_element_by_accessibility_id('SomeAccessibilityID').get_attribute('content-desc')

el1 = driver.find_element_by_accessibility_id("Press")
el1.click()

sleep(1)
el1.click()
sleep(1)
el1.click()
sleep(1)
el1.click()
sleep(1)
el1.click()

# Assertions
text = driver.find_element_by_accessibility_id("LayoutDiff is cool!")