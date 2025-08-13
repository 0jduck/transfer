# imports
import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional

# time cmd cog
class time_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /time cmd
    @app_commands.command(name="time", description="Gets a discord time stamp")
    @app_commands.describe(time_of_day="Provide a time of day, HH:MM format", timezone="Provide a time zone.")
    @app_commands.choices(
        timezone=[
            app_commands.Choice(name="GMT", value="0"),
            app_commands.Choice(name="EST", value="-5"),
            app_commands.Choice(name="PST", value="-8"),
            app_commands.Choice(name="CET", value="1")
        ]
    )
    async def time(self, interaction: discord.Interaction, time_of_day: str, timezone: Optional[str] = None):
        try:                   
            hours, minutes = map(int, time_of_day.split(":"))
            timezone = int(timezone) if timezone else 0
            timestamp = ((hours - timezone) * 60 * 60) + (minutes * 60)
            embed = discord.Embed(
                title="Timestamp made",
                description=f"A timestamp for {time_of_day} was made.\n`<t:{timestamp}:t>`",
                color=discord.Color.dark_green()
            )
        except ValueError as e:
            embed = discord.Embed(
                title="Error",
                description=f"Value error: {e}",
                color=discord.Color.dark_red()
            )
        except Exception as e:
            embed = discord.Embed(
                title="Error",
                description=f"Error: {e}",
                color=discord.Color.dark_red()
            )
        await interaction.response.send_message(embed=embed)
    
# add cog
async def setup(bot):
    await bot.add_cog(time_cog(bot))