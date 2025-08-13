# imports
import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional
import aiohttp
import json

# api cmd cog
class rule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # ? rule cmd
    @commands.command(name='rule')
    async def hello(self, ctx, number: int):
        reply = {
            'error': '**Error** - Bad input',
            '1': '1. **Follow Discords Terms Of Service** - Follow and don’t break, condone, encourage or support breaking https://discord.com/terms.',
            '2': '2. **Nothing Hateful Or Rude** - Any form of hate or toxicity is not tolerated or allowed. Be nice, welcoming and open.',
            '3': '3. **No Repetitive Messages Or Actions** - Don’t send repetitive messages or do actions that can count as message spam, mention spam, character spam, reaction spam or other forms of spam.',
            '4': '4. **Keep Personal Information Personal** - Don’t share your own or other personal information. Do not attempt to get ahold of others personal information.',
            '5': '5. **Keep It SFW And Appropriate** - All you do in this server or that is on your profile needs to be SFW (Safe For Work) and appropriate.',
            '6': '6. **No Impersonation** - Impersonating other users, people, staff, bots and so on is not acceptable if done with malicious intent.',
            '7': '7. **Use Correctly** - Use the correct channels, tags, pings and similar stuff for the correct use.',
            '8': '8. **Don’t Discuss Controversial Topics** - Don’t discuss topics like religion, politics and other “controversial” or “sensitive” topics.'
        }
        if number > 0 and number < 9:
            reply = reply[str(number)]
        else:
            reply = reply["error"]
        await ctx.send(str(reply))


# add cog
async def setup(bot):
    await bot.add_cog(rule(bot))