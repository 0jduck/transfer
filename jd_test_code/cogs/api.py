# imports
import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional
import aiohttp
import json

# api cmd cog
class api_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # /api cmd
    @app_commands.command(name="api", description="Fetches info from the API")
    @app_commands.describe(key='The api key')
    async def api(self, interaction: discord.Interaction, key: Optional[str] = None):
        if key:
            key = {
                "key": key
            }
            url = "https://jduck.pythonanywhere.com/api/key"
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=key) as response:
                    data = await response.json()
                    await interaction.response.send_message(response)
        else:
            url = "https://jduck.pythonanywhere.com/api"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    await interaction.response.send_message(data)

# add cog
async def setup(bot):
    await bot.add_cog(api_cog(bot))

