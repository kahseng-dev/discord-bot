from discord import Embed
from utils.host_server import get_status

def server_info_embed():
    ip = "sanctuary.play.hosting"
    status = get_status()
    version = "1.21.1"
    modpack = "Cobblemon Official Modpack [Fabric]"

    how_to_play = (
        "Download the Cobblemon Official Modpack [Fabric]! (required) \n" \
        "- [modrinth](<https://modrinth.com/modpack/cobblemon-fabric/versions>) \n" \
        "- [curseforge](<https://www.curseforge.com/minecraft/modpacks/cobblemon-fabric/files/all?page=1&pageSize=20>) \n" \
        "Simple Voice Chat supported! (optional) \n" \
        "- [modrinth](<https://modrinth.com/plugin/simple-voice-chat/versions>) \n" \
        "- [curseforge](<https://www.curseforge.com/minecraft/mc-mods/simple-voice-chat/files/all?page=1&pageSize=20>) \n" \
    )

    discord_commands = (
        "`!start` - if the server is offline, the bot will turn it on \n" \
    )

    info = (
        f"IP: `{ip}` \n" \
        f"Status: `{status}` \n" \
        f"Minecraft Version: `{version}` \n" \
        f"Currently Running: `{modpack}` \n" \
        "-# It's recommended to use Prism Launcher to auto update the modpack."
    )

    embed = Embed(title="Server Info")
    embed.add_field(name="How to play", value=how_to_play, inline=False)
    embed.add_field(name="Discord Commands", value=discord_commands, inline=False)
    embed.add_field(name="Info", value=info, inline=False)
    
    return embed