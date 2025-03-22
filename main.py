import os
import discord
import webserver
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

command_prefix = "!"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix, intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    try:
        print(f"[SUCCESS]: {bot.user} is online")
        await bot.tree.sync()
        print(f"[SUCCESS]: Synced commands.")
    except Exception as error:
        print(f"[ERROR]: {error}")

@tree.command(name = "ping", description = "Checks ping")
async def ping(interaction):
    await interaction.response.send_message(f"[SUCCESS]: Pong!")

@tree.command(name = "start", description = "Starts minecraft server when it is offline")
async def start(interaction):
    await interaction.response.send_message(f"[SUCCESS]: Its working!")

webserver.keep_awake()
bot.run(DISCORD_TOKEN)