import discord
from discord.ext import commands
import random
from cogs.utils import checks
from data.code import minecraft

class set:
    """ wait"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)
    @checks.is_main_server()
    async def givealt(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅")
        await self.bot.whisper(random.choice(minecraft.minecraft_accounts))

def setup(bot):
    
	bot.add_cog(set(bot))
