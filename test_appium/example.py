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
    "platformVersion": "9",
    "deviceName": args.device_name,
    "app": args.apk_path,
    "appPackage": "com.example.layoutdiffexample",
    "appActivity": ".MainActivity",
    "automationName": "UiAutomator2"
}

# Instantiating the appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def save_screenshot(screenshot_name, element=None):
    """Save a screenshont from the tested application"""
    sleep(1)  # Wait for end of animations 

    if not element:
        # Get the root element
        element = driver.find_elements_by_xpath("//*")[0]

    # Taking screenshot
    image_path = f"{args.screenshot_path}/{screenshot_name}.png"
    full_image = io.BytesIO(base64.b64decode(driver.get_screenshot_as_base64()))
    pil_image = Image.open(full_image)
    
    # Get element coordinates on device screen
    element_x, element_y = element.location["x"], element.location["y"]
    element_width, element_height = element.size["width"], element.size["height"]

    # Remove OS status bar from screenshot
    status_bar_data = driver.get_system_bars()['statusBar']
    if status_bar_data['visible'] and element_x <= status_bar_data["x"] and element_y <= status_bar_data["y"]:
        element_y = status_bar_data["y"] + status_bar_data["height"]
        element_height += status_bar_data["height"]
    
    # Save element image
    element_crop = pil_image.crop((element_x, element_y, element_width+element_x, element_height+element_y))
    element_crop.save(image_path)

driver.implicitly_wait(10)  # Set the amount of time the driver should wait when searching for elements (it's optional)

# Generated test script
el1 = driver.find_element_by_accessibility_id("Press")
el1.click()

save_screenshot("press_button", element=el1)
save_screenshot("home_screen_click_blue")

sleep(1)
el1.click()
save_screenshot("home_screen_click_green")

sleep(1)
el1.click()
save_screenshot("home_screen_click_yellow")

sleep(1)
el1.click()
save_screenshot("home_screen_click_red")

sleep(1)
el1.click()
save_screenshot("home_screen_click_brown")