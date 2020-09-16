import discord
from discord.ext import commands


class SongBotClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.guild = None

    async def on_ready(self):
        if len(self.guilds) == 0:
            raise RuntimeError("Connected, but there are no client guilds.")
        elif len(self.guilds) >= 2:
            raise RuntimeError("Connected, but there is more than one client guild.")
        else:
            self.guild = self.guilds[0]
            print(f"{self.user} has connected to guild {self.guild.name} with id {self.guild.id}.")

    async def on_message(self, message):
        if message.author == self.user:
            return

        content = message.content
        if content.startswith("~echo ") and len(content) > 6:
            await message.channel.send(content[6:])
