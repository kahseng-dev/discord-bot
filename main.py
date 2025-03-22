import os
import discord
import webserver
import asyncio
from dotenv import load_dotenv
from discord import app_commands
from discord.ext.commands import Bot

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

command_prefix = "!"
bot = Bot(command_prefix, intents=discord.Intents.default())

@bot.event
async def on_ready():
    try:
        print(f"[SUCCESS]: {bot.user} is online")
        for server in bot.guilds:
            await bot.tree.sync(guild=discord.Object(id=server.id))
            print(f"[SUCCESS]: Synced commands.")
    except Exception as error:
        print(f"[ERROR]: {error}")

@bot.tree.command(name = "ping", description = "Checks ping")
async def ping(interaction):
    await interaction.response.send_message(f"[SUCCESS]: Pong!")

@bot.tree.command(name = "start", description = "Starts minecraft server when it is offline")
async def start(interaction):
    await interaction.response.send_message(f"[SUCCESS]: Its working!")

webserver.keep_awake()
bot.run(DISCORD_TOKEN)