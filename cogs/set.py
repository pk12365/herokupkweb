import random
import discord
from cogs.utils import checks
from data.code import minecraft, spotify, netflix, hulu, origin, uplay
from discord.ext import commands

class get:
    """ wait"""

    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True, name="givealt", aliases=["helpalt", "althelp", "getalt", "Getalt", "GETALT", "Helpalt", "HelpAlt", "HELPALT", "altHelp", "altHELP", "ALTHELP"])
    async def givealt(self, ctx):
        """Get Free Accounts"""
        author = ctx.message.author
        line1 = ("we are giving some 🆓alt only on\n💟INDIAN CYBER WORLD💟\nit u not on thare join fast\nhttps://discord.gg/tdfKtax\nJust take a command $get(your command)\n\nAccount List🔻\n🔴minecraft\n🔵Spotify\n⚪Netflix\n⚫Hulu\n🔴Origin\n🔵Uplay.")
        field_name = "Generic Name"
        field_contents = "Example contents for this field"
        footer_text = ""

        embed = discord.Embed(colour=0xFF0000, description=line1)
        embed.title = "INDIAN CYBER WORLD"
        embed.set_footer(text=footer_text)
        await self.bot.say(embed=embed)

    @commands.command(no_pm=True, name="getminecraft", aliases=["getMinecraft", "GetMinecraft", "GETMINECRAFT"])
    @checks.is_main_server()
    @commands.cooldown(1, 600, type=commands.BucketType.user)
    async def getminecraft(self):
        """For minecraft accounts"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(minecraft.minecraft_accounts))

    @commands.command(no_pm=True, name="getspotify", aliases=["getSpotify", "GetSpotify", "GETSPOTIFY"])
    @checks.is_main_server()
    @commands.cooldown(1, 600, type=commands.BucketType.user)
    async def getspotify(self):
        """For spotify accounts"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(spotify.spotify_accounts))

    @commands.command(no_pm=True, name="getnetflix", aliases=["getNetflix", "GetNetflix", "GETNETFLIX"])
    @checks.is_main_server()
    @commands.cooldown(1, 600, type=commands.BucketType.user)
    async def getnetflix(self):
        """For netflix accounts"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(netflix.netflix_accounts))

    @commands.command(no_pm=True, name="gethulu", aliases=["getHulu", "GetHulu", "GETHULU"])
    @checks.is_main_server()
    @commands.cooldown(1, 600, type=commands.BucketType.user)
    async def gethulu(self):
        """For hulu accounts"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(hulu.hulu_accounts))

    @commands.command(no_pm=True, name="getorigin", aliases=["getOrigin", "GetORIGIN", "GETORIGIN"])
    @checks.is_main_server()
    @commands.cooldown(1, 600, type=commands.BucketType.user)
    async def getorigin(self):
        """For origin accounts"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(origin.origin_accounts))

    @commands.command(no_pm=True, name="getuplay", aliases=["getUplay", "GetUplay", "GETUPLAY"])
    @checks.is_main_server()
    @commands.cooldown(1, 600, type=commands.BucketType.user)
    async def getuplay(self):
        """For uplay accouns"""

        #Your code will go here
        await self.bot.say("check your dm bebe 😅😅", delete_after=5.0)
        await self.bot.whisper(random.choice(uplay.uplay_accounts))
def setup(bot):
    bot.add_cog(get(bot))
