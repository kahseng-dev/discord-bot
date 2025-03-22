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
    await interaction.response.send_message(f"[INFO]: Not implemented yet")

webserver.keep_awake()
bot.run(DISCORD_TOKEN)