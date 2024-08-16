from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import asyncio
from bs4 import BeautifulSoup as Soup
import os
import requests

USERNAME = "0x492024"
PASSWORD = "nypbuw-cuxjyc-peMbe5"

# Initialize FirefoxOptions
options = Options()
options.add_argument("--width=800")
options.add_argument("--height=1440")
# options.add_argument('--headless=new')
# options.add_argument('log-level=3')
# Creating an instance webdriver
driver = webdriver.Firefox(options=options) 
# driver.set_window_size(1920, 1080)
driver.set_window_position(-1440,0)
driver.get('https://www.instagram.com')

# Let's the user see and also load the element 
time.sleep(2)

# Login function
async def login():    
    #Find username input area and write username
    username = WebDriverWait(driver, timeout=60).until(
        lambda d: d.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
    username.send_keys(USERNAME)

    #Find password input area and write password
    password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys(PASSWORD)

    #Click on Login Button
    enter = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    enter.click()
    print("Logged in")
    time.sleep(5)

# Find all images, and disable display.
async def disable_images():
    images = driver.find_elements(By.CSS_SELECTOR, 'img')
    for img in images:
        driver.execute_script("arguments[0].style.display = 'none';", img)
        # find image 's parent element and change background color to green
        driver.execute_script("arguments[0].style.backgroundColor = '#0F0';", img.find_element(By.XPATH, '..'))

# Not store and not notification
async def click_not_now():
    notStore = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div')
    notStore.click()
    print("Not Now Store")
    time.sleep(3)

    # notNotification = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    # notNotification.click()
    notNotification = driver.find_element(By.CSS_SELECTOR, '._a9_1')
    notNotification.click()
    print("Not Now Notification")
    # time.sleep(5)

# Search, click search and type in search and click on first user
async def my_search():
    search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div')
    search.click()
    print("Click Search")
    await asyncio.sleep(1)
    await disable_images()
    await asyncio.sleep(.5)
   
    search_user = "貓"
    search_input = WebDriverWait(driver, timeout=60).until(
        lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))
    search_input.send_keys(search_user)
    print("Type in Search")
    await asyncio.sleep(1)
    await disable_images()
    await asyncio.sleep(.5)

    found = WebDriverWait(driver, timeout=60).until(
        lambda d: d.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]'))
    found.click()
    print("Click on First User")
    # time.sleep(5)
    await asyncio.sleep(1)
    await disable_images()
    await asyncio.sleep(.5)

#Download all images
async def download_images():
    # Get page source
    page_source = driver.page_source
    # Parse HTML
    soup = Soup(page_source, 'html.parser')
    # Find all images
    images = soup.find_all('img')
    # Download all images
    for index, image in enumerate(images):
        try:
            # Get image source
            image_src = image['src']
            # print(image_src)
            # Download image
            img_r = requests.get(image_src, stream=True)
            with open(f'images/{index}.png', 'wb') as f:
                f.write(img_r.content)
        except:
            pass


# Scroll down
async def scroll_down(timeout):
    scroll_pause_time = timeout
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    print("last_height", last_height)
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
        # Wait to load page
        await asyncio.sleep(scroll_pause_time)
        await disable_images()
        await download_images()
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        print("new_height", new_height)
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height
        print("Stop scrolling")


# Main function
async def main():
    await login()
    await asyncio.sleep(1)
    await click_not_now()
    await asyncio.sleep(1)
    await disable_images()
    # await my_search()
    # await asyncio.sleep(1)
    await scroll_down(5)

asyncio.run(main())
