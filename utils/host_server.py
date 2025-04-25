import os
import asyncio

from seleniumbase import Driver
from seleniumbase.common.exceptions import NoSuchElementException

from dotenv import load_dotenv

load_dotenv()
HOST_USERNAME = os.getenv('HOST_USERNAME')
HOST_PASSWORD = os.getenv('HOST_PASSWORD')
SERVER_ID = os.getenv('SERVER_ID')

status = "LIMBO"
headless = False

driver = Driver(uc=True)
if headless:
    driver.add_argument("--headless")

def get_status():
    global status

    url = "https://panel.play.hosting/server"
    driver.get(f"{url}/{SERVER_ID}")

    status_by_text = {
        "LIMBO" : "Join Queue",
        "QUEUE" : "Leave Queue",
        "OFFLINE" : "Server marked as offline..",
        "STARTING" : "Server marked as starting..",
        "ONLINE" : "Server marked as running..",
        "ONLINE" : "[Server thread/INFO]: Done"
    }

    for state, text in status_by_text.items():
        try:
            if driver.is_text_visible(text):
                status = state
                print(f"[INFO] Server status: {status}")
                break
        except NoSuchElementException:
            pass
    
    return status

async def connect_account():
    url = "https://panel.play.hosting/auth/login"
    driver.get(url)
    asyncio.sleep(1)

    driver.type('input[name="username"]', HOST_USERNAME)
    driver.type('input[name="password"]', HOST_PASSWORD)
    asyncio.sleep(1)

    driver.click('button:contains("Login")')
    asyncio.sleep(2)

    return print(f"[✓] Connected to account")

async def start_server():
    check_interval = 20

    while status != "ONLINE":
        get_status()

        match status:
            case "LIMBO":
                driver.click('button:contains("Join Queue")')
            case "QUEUE":
                pass
            case "OFFLINE":
                driver.click('button:contains("Start")')
            case "STARTING":
                pass
            case "ONLINE":
                break
            case _:
                print(f"[ERROR] Unknown status: {status}")
                break

        asyncio.sleep(check_interval)
        driver.refresh()
        print("Refreshing page...")