import discord
from discord.ext import commands
import random
messages = ["Message 0", "Message 1", "Message 2"]
class set:
    """ wait"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)
    async def givealt(self):
        """done"""

        #Your code will go here
        await self.bot.whisper(random.choice(messages))

def setup(bot):
    bot.add_cog(set(bot))
