import os
import discord
from commands import Commands

TOKEN = os.getenv('DISCORD_TOKEN')

class DiscordClient(discord.Client, Commands):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    def run_bot(self):
        self.run(TOKEN)