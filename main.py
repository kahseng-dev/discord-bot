import os
import discord
import webserver
import asyncio
import logging
import undetected_chromedriver as uc
from dotenv import load_dotenv
from discord import app_commands
from discord.ext.commands import Bot
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
log = logging.getLogger(__name__)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
HOST_USERNAME = os.getenv("HOST_USERNAME")
HOST_PASSWORD = os.getenv("HOST_PASSWORD")
SERVER_ID = os.getenv("SERVER_ID")

command_prefix = "!"
intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix, intents=intents)

@bot.event
async def on_ready():
    try:
        log.info(f"[SUCCESS]: {bot.user} is online")
        await bot.tree.sync()
        log.info(f"[SUCCESS]: Synced commands.")
    except Exception as error:
        log.error(f"[ERROR]: {error}")

@bot.tree.command(name = "ping", description = "Checks ping")
async def ping(interaction):
    await interaction.response.send_message(f"Pong!")
    log.info(f"[SUCCESS]: Pong!")

@bot.tree.command(name = "start", description = "Starts minecraft server when it is offline")
async def start(interaction):
    options = webdriver.ChromeOptions() 
    options.headless = True
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = uc.Chrome(options=options)

    website = "https://panel.play.hosting/server"
    website_auth = "https://panel.play.hosting/auth/login"

    website_username = driver.find_element(By.NAME, "username")
    website_password = driver.find_element(By.NAME, "password")
    website_loginButton = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div/div/div[4]/button")

    driver.get(website_auth)
    website_username.send_keys(HOST_USERNAME)
    website_password.send_keys(HOST_PASSWORD)
    website_loginButton.click()

    driver.execute_script(f"window.open({website}/{SERVER_ID},'_blank');")
    driver.switch_to.window(driver.window_handles[1])

    server_status = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div/div/h2").text

    print(server_status)

    if (server_status == "Server in Limbo"):
        return

    driver.close()
    await interaction.response.send_message(f"[INFO]: Not implemented yet")

@bot.tree.command(name = "status", description = "Display minecraft server status")
async def status(interaction):
    await interaction.response.send_message(f"[INFO]: Not implemented yet")

@bot.tree.command(name = "server-info", description = "Minecraft server information")
async def server_info(interaction):
    server_ip = "sanctuary.play.hosting"
    server_modpack = "Cobblemon Official Modpack [Fabric] 1.21.1"
    message = (f"""# Server Info
## How to play
**Download the Cobblemon Official Modpack [Fabric]! (required)**
- [modrinth](<https://modrinth.com/modpack/cobblemon-fabric/versions>)
- [curseforge](<https://www.curseforge.com/minecraft/modpacks/cobblemon-fabric/files/all?page=1&pageSize=20>)
**Simple Voice Chat supported! (optional)**
- [modrinth](<https://modrinth.com/plugin/simple-voice-chat/versions>)
- [curseforge](<https://www.curseforge.com/minecraft/mc-mods/simple-voice-chat/files/all?page=1&pageSize=20>)
## Discord Commands
`/start` - if the server is offline, the bot will turn it on
`/status` - show status of the server
## Server IP: `{server_ip}`
currently running: `{server_modpack}`

-# recommended to use Prism Launcher to manage and auto update minecraft instances."""
    )
    await interaction.response.send_message(message)
    log.info(f"[SUCCESS]: Bot has posted server info")

webserver.keep_awake()
bot.run(DISCORD_TOKEN)