# imports
import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional

# info cmd cog
class note_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # /note cmd
    @app_commands.command(name="note", description="Notes something down")
    @app_commands.describe(body='The body/main text of the note', title="The title/name of the note")
    async def note(self, interaction: discord.Interaction, body: str, title: Optional[str] = None):
        embed = discord.Embed(
            title='User Made Note',
            description=f'User made a note, body was: `{body}`'
        )
        if title:
            embed.description = f'User made a note:\n**title** - `{title}`\nbody - `{body}`'
        try:
            await interaction.user.send(embed=embed)
        except:
            embed.description = 'Failed to send direct message.'
        await interaction.response.send_message(embed=embed)

# add cog
async def setup(bot):
    await bot.add_cog(note_cog(bot))