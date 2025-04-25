import discord
import os
import asyncio

from dotenv import load_dotenv
from discord.ext import commands, tasks

from utils.embeds import server_info_embed
from utils.web_service import keep_awake

from utils.host_server import get_status
from utils.host_server import connect_account
from utils.host_server import start_server

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

host_name = "play.hosting"

intents = discord.Intents.default()
intents.message_content = True
description = 'A simple bot to manage your own minecraft server from a hosting service.'

bot = commands.Bot(command_prefix = "!", 
                   intents=intents,
                   description=description,
                   case_insensitive=True,
                   help_command=None)

@bot.event
async def on_ready():
    print(f"[✓] {bot.user} is online")

    print(f"[INFO] Syncing slash commands...")
    await bot.tree.sync()
    print(f"[✓] Synced slash commands")

    print(f"[INFO] Logging into {host_name}...")

    await connect_account()
    get_status()

@bot.command(name='info', aliases=['i'])
async def info(ctx: commands.Context):
    print(f"[INFO] Sending server info embed...")
    await ctx.send(embed=server_info_embed())
    print(f"[✓] Sent server info embed")

@bot.command(name='start', aliases=['s'])
async def start(ctx: commands.Context):
    print(f"[INFO] Starting server...")
    message = await ctx.send("Starting server...")
    await start_server()

keep_awake()
bot.run(DISCORD_TOKEN)