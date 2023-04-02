import os

import discord
from dotenv import load_dotenv

from CCCCCCBot import CCCCCCBot
from discord.ext import commands

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)
    bot.add_cog(CCCCCCBot(bot))
    bot.run(TOKEN)
