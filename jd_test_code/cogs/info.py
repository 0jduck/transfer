# imports
import discord
from discord import app_commands
from discord.ext import commands

# info cmd cog
class info_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # /info cmd
    @app_commands.command(name="info", description="Get bot info")
    async def info(self, interaction: discord.Interaction):
        # make embed
        embed = discord.Embed(
            title="Info",
            description="I am a bot!",
            color=discord.Color.dark_green()
        )
        # send reply
        await interaction.response.send_message(embed=embed)
    
# add cog
async def setup(bot):
    await bot.add_cog(info_cog(bot))