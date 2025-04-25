import os
import asyncio

from seleniumbase import Driver
from seleniumbase.common.exceptions import NoSuchElementException

from dotenv import load_dotenv

load_dotenv()
HOST_USERNAME = os.getenv('HOST_USERNAME')
HOST_PASSWORD = os.getenv('HOST_PASSWORD')
SERVER_ID = os.getenv('SERVER_ID')

status = "OFFLINE"
headless = False

driver = Driver(uc=True)
if headless:
    driver.add_argument("--headless")

def get_status():
    print(driver.is_element_present('div:contains("Server marked as running..")'))

    return status

async def connect_account():
    url = "https://panel.play.hosting/auth/login"
    driver.get(url)
    await asyncio.sleep(1)

    driver.type('input[name="username"]', HOST_USERNAME)
    driver.type('input[name="password"]', HOST_PASSWORD)
    await asyncio.sleep(1)

    driver.click('button:contains("Login")')
    await asyncio.sleep(2)

    return print(f"[✓] Connected to account")

async def start_server():
    url = "https://panel.play.hosting/server"
    driver.get(f"{url}/{SERVER_ID}")
    status = get_status()

    match status:
        case "OFFLINE":
            print("Server is offline...")
            driver.click('button:contains("Start")')
        case "ONLINE":
            print("Server is online...")
        case "STARTING":
            print("Server is starting...")

asyncio.run(connect_account())