import random

import discord
from cogs.utils import checks
from data.code import minecraft, spotify, netflix, hulu, origin, uplay
from discord.ext import commands

class set:
    """ wait"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name="getalt",
                      aliases=["helpalt", "althelp", "getalt", "Getalt", "GETALT", "Helpalt", "HelpAlt", "HELPALT", "altHelp", "altHELP", "ALTHELP"])
    @checks.is_main_server()
    async def getalt(self):

        #Your code will go here
        await self.bot.say('```we are giving some 🆓alt only on\n💟INDIAN CYBER WORLD💟\nJust take a command $get(your command)\n\nAccount List⤵\n\n🔴minecraft\n🔵Spotify\n⚪Netflix\n⚫Hulu\n🔴Origin\n🔵Uplay```')

    @commands.command(no_pm=True, name="getminecraft", aliases=["getMinecraft", "getMINECRAFT"])
    @checks.is_main_server()
    async def getminecraft(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(minecraft.minecraft_accounts))

    @commands.command(no_pm=True, name="getspotify", aliases=["getSpotify", "getSPOTIFY", "GETSPOTIFY"])
    @checks.is_main_server()
    async def getspotify(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(spotify.spotify_accounts))

    @commands.command(no_pm=True, name="getnetflix", aliases=["getNetflix", "getNETFLIX", "GETNETFLIX"])
    @checks.is_main_server()
    async def getnetflix(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(netflix.netflix_accounts))

    @commands.command(no_pm=True, name="hulu", aliases=["getHulu", "getHULU", "GETHULU"])
    @checks.is_main_server()
    async def gethulu(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(hulu.hulu_accounts))

    @commands.command(no_pm=True, name="origin", aliases=["getOrigin", "getORIGIN", "GETORIGIN"])
    @checks.is_main_server()
    async def getorigin(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(origin.origin_accounts))

    @commands.command(no_pm=True, name="getuplay", aliases=["getUplay", "getUPLAY", "GETUPLAY"])
    @checks.is_main_server()
    async def getuplay(self):
        """done"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(uplay.uplay_accounts))
def setup(bot):
    bot.add_cog(set(bot))
