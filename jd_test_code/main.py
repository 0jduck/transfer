# imports
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
import os


# Run bot
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
intents.dm_messages = True
intents.guild_reactions = True
intents.dm_reactions = True
intents.members = True
intents.presences = True
intents.guild_typing = True
intents.dm_typing = True

client = commands.Bot(command_prefix="?", intents=intents)

# on start
@client.event
async def on_ready():
  # set presence and sync cmds
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="for /info"))
  print('[Presence Changed]')
  await client.tree.sync(guild=discord.Object(id=1304484540055818284))
  await client.tree.sync()
  print('[Commands Synced]')


# Run bot
async def run_bot():
  cogs_load = [
    'info',
    'note',
    'rule',
    'time'
  ]
  for i in range(len(cogs_load)):
    try:
      await client.load_extension('cogs.' + cogs_load[i])
    except Exception as e:
      print(f"[Cog '{cogs_load[i]}' Error] {e}")
  print('[Cogs Loaded]')
  load_dotenv()
  print('[Bot starting]')
  await client.start(os.getenv('bot_key'))
try:
  asyncio.run(run_bot())
except KeyboardInterrupt:
  print('[Bot Stopped] KeyboardInterrupt')
except Exception as e:
  print(f'[Bot Stopped]  Error: {e}')

