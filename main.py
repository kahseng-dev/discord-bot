import os
import discord
import webserver
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

command_prefix = "!"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix, intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"TEST: {bot.user} is online!")

@bot.tree.command(name="say_working", description="TEST COMMAND: literal says its working")
async def say_working(interaction: discord.Interaction):
    username = interaction.user.mention
    await interaction.response.send_message(f"Its working!, {username}")

webserver.keep_awake()
bot.run(DISCORD_TOKEN)