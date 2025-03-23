import os
import discord
import webserver
import asyncio
import logging
from dotenv import load_dotenv
from discord import app_commands
from discord.ext.commands import Bot

load_dotenv()
log = logging.getLogger(__name__)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

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
    await interaction.response.send_message(f"[SUCCESS]: Pong!")

@bot.tree.command(name = "start", description = "Starts minecraft server when it is offline")
async def start(interaction):
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