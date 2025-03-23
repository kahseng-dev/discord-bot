@bot.tree.command(name = "ping", description = "Checks ping")
async def ping(interaction):
    await interaction.response.send_message(f"Pong!")
    log.info(f"[SUCCESS]: Pong!")