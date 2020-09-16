import discord


class SongBotClient(discord.Client):

    def __init__(self):
        discord.Client.__init__(self)
        self.guild = None

    async def on_ready(self):
        if len(self.guilds) == 0:
            raise RuntimeError("Connected, but there are no client guilds.")
        elif len(self.guilds) >= 2:
            raise RuntimeError("Connected, but there is more than one client guild.")
        else:
            self.guild = self.guilds[0]
            print(f"{self.user} has connected to guild {self.guild}.")
