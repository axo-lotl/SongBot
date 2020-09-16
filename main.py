import discord
import os
import time
from dotenv import load_dotenv
from songbot import SongBotClient


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('DISCORD_BOT_TOKEN')

    song_bot_client = SongBotClient()
    song_bot_client.run(token)

