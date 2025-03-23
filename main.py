import os
import discord
import webserver
import asyncio
import logging
from dotenv import load_dotenv
from discord import app_commands
from discord.ext.commands import Bot
from seleniumbase import SB

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
    except Exception as exception:
        log.error(f"[ERROR]: {exception}")

@bot.tree.command(name = "start", description = "Starts minecraft server when it is offline")
async def start(interaction):
    site = "https://panel.play.hosting/server"
    site_auth = "https://panel.play.hosting/auth/login"

    try:
        with SB(uc=True, headless=True, xvfb=True) as sb:
            sb.activate_cdp_mode(site_auth)
            sb.sleep(0.2)
            sb.type('[name="username"]', HOST_USERNAME)
            sb.type('[name="password"]', HOST_PASSWORD)
            sb.sleep(0.2)
            sb.uc_gui_click_captcha()
            sb.click('button:contains("Login")')
            sb.sleep(1)
            sb.goto(f"{site}/{SERVER_ID}")

            if sb.is_element_present('span:contains("Server marked as running...")'):
                log.info(f"[SUCCESS]: Server is online!")
                await interaction.response.send_message(f"[SUCCESS]: Server is online!")
            
            elif sb.is_element_present('span:contains("Server marked as starting..")'):
                log.info(f"[INFO]: Server is in the process of starting")
                await interaction.response.send_message(f"[INFO]: Server is in the process of starting")
                while not sb.is_element_present('span:contains("Server marked as running...")'):
                    sb.wait_for_element('span:contains("Server marked as running...")')
                    sb.refresh()

            elif sb.is_element_present("div.xterm-screen") or sb.is_element_present('span:contains("Server marked as offline..'):
                log.info(f"[INFO]: Terminal is present")
                log.info(f"[INFO]: Starting server...")
                await interaction.response.send_message(f"[INFO]: Starting server...")
                sb.click('button:contains("Start")')
                while not sb.is_element_present('span:contains("Server marked as running...")'):
                    sb.wait_for_element('span:contains("Server marked as running...")')
                    sb.refresh()
            
            elif sb.is_element_present('button:contains("Leave Queue")'):
                log.info(f"[INFO]: Still in queue...")
                await interaction.response.send_message(f"[INFO]: Still in queue...")

                while not sb.is_element_present("div.xterm-screen"):
                    sb.wait_for_element("div.xterm-screen")
                    sb.refresh()
            
            elif sb.is_element_present('button:contains("Join Queue")'):
                log.info(f"[INFO]: Server is in Limbo")
                log.info(f"[INFO]: Joining queue...")
                await interaction.response.send_message(f"[INFO]: Server is in Limbo")
                await interaction.response.send_message(f"[INFO]: Joining queue...")
                sb.click('button:contains("Join Queue")')

                while not sb.is_element_present("div.xterm-screen"):
                    sb.wait_for_element("div.xterm-screen")
                    sb.refresh()
                    
    except Exception as exception:
        log.error(f"[ERROR]: {exception}")
    
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
## Server IP: `{server_ip}`
currently running: `{server_modpack}`

-# recommended to use Prism Launcher to manage and auto update minecraft instances."""
    )
    await interaction.response.send_message(message)
    log.info(f"[SUCCESS]: Bot has posted server info")

webserver.keep_awake()
bot.run(DISCORD_TOKEN)