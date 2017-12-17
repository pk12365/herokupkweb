import random
import discord
from cogs.utils import checks
from data.code import minecraft, spotify, netflix, hulu, origin, uplay
from discord.ext import commands

class set:
    """ wait"""

    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True, name="givealt", aliases=["helpalt", "althelp", "Getalt", "GETALT", "Helpalt", "HelpAlt", "HELPALT", "altHelp", "altHELP", "ALTHELP"])
    async def givealt(self):

        #Your code will go here
        await self.bot.say('```we are giving some 🆓alt only on\n💟INDIAN CYBER WORLD💟\nit u not on thare join fast https://discord.gg/tdfKtax\nJust take a command $get(your command)\n\nAccount List⤵\n\n🔴minecraft\n🔵Spotify\n⚪Netflix\n⚫Hulu\n🔴Origin\n🔵Uplay```')

    @commands.command(no_pm=True)
    @checks.is_main_server()
    async def getminecraft(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(minecraft.minecraft_accounts))

    @commands.command(no_pm=True)
    @checks.is_main_server()
    async def getspotify(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(spotify.spotify_accounts))

    @commands.command(no_pm=True)
    @checks.is_main_server()
    async def getnetflix(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(netflix.netflix_accounts))

    @commands.command(no_pm=True)
    @checks.is_main_server()
    async def gethulu(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(hulu.hulu_accounts))

    @commands.command(no_pm=True)
    @checks.is_main_server()
    async def getorigin(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(origin.origin_accounts))

    @commands.command(no_pm=True)
    @checks.is_main_server()
    async def getuplay(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(uplay.uplay_accounts))
def setup(bot):
    bot.add_cog(set(bot))
