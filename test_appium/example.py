import argparse, io, base64
from PIL import Image
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

def save_screenshot(element, screenshot_name):
    """Save a screenshont from the tested application"""
    sleep(1)  # Wait for end of animations 
    image_path = f"{args.screenshot_path}/{screenshot_name}.png"
    full_image = io.StringIO(base64.b64decode(driver.get_screenshot_as_base64()))
    pil_image = Image.open(full_image)
    element_x, element_y = element.location
    element_width, element_height = element.size
    element_crop = pil_image.crop((element_x, element_y, element_width, element_height))
    element_crop.save(image_path)

driver.implicitly_wait(10)  # Set the amount of time the driver should wait when searching for elements (it's optional)

# Generated test script
save_screenshot("home_screen")
el1 = driver.find_element_by_accessibility_id("Press")
el1.click()
save_screenshot(driver.find_elements_by_xpath("/*"), "home_screen_click_blue")
save_screenshot(el1, "press_button_blue")

sleep(1)
el1.click()
save_screenshot(driver.find_elements_by_xpath("/*"), "home_screen_click_green")
save_screenshot(el1, "press_button_green")

sleep(1)
el1.click()
save_screenshot(driver.find_elements_by_xpath("/*"), "home_screen_click_yellow")
save_screenshot(el1, "press_button_yellow")

sleep(1)
el1.click()
save_screenshot(driver.find_elements_by_xpath("/*"), "home_screen_click_red")
save_screenshot(el1, "press_button_red")

sleep(1)
el1.click()
save_screenshot(driver.find_elements_by_xpath("/*"), "home_screen_click_brown")
save_screenshot(el1, "press_button_brown")