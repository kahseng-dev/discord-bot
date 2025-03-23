# Discord Bot

> private discord bot that manages external automated tasks

<img alt="discord" src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=fff"/> <img alt="python" src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=fff"/> <img alt="render" src="https://img.shields.io/badge/render-000000?style=for-the-badge&logo=render&logoColor=fff"/> <img alt="selenium" src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=fff"/> 

## Installation

1. Install dependencies with `$ pip install -r requirement.txt`

2. Copy `.env.example` to `.env` and start filling in the values as detailed

3. Discord Developer portal permissions
    - OAuth2 URL Generator
        - `bot`
        - `applications.commands`
    - Bot Permissions
        - `Send Messages`
        - `Use Slash Commands`
    - Privileged Gateway Intents
        - `Message Content Intent`

4. Ensure that the channels your bots have access to allow the bot to have these permissions.
    - `Send Messages`
    - `Use Application Commands`