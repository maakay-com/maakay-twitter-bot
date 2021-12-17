import os
import django

'''
Import external dependencies here. Eg:

import discord
from discord_slash import SlashCommand

'''

# Django Setup on bot
DJANGO_DIRECTORY = os.getcwd()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ["DJANGO_SETTINGS_MODULE"])
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

'''
Import Django related packages here. Example:

from django.conf import settings
from core.utils.scan_chain import match_transaction, check_confirmation, scan_chain

'''

'''
Your Twitter/ Discord token imported from environment variable

TOKEN = os.environ['TOKEN']
'''

# Initialize the Twitter/ Discord Bot
'''
Discord Bot definition example

bot = commands.Bot(command_prefix=">")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("------------------------------------")
    print("Bot Running:")
    print("------------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="/help"))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

'''

# Write the slash commands/ twitter commands here.

'''
Run the bot code here.

Discord Example: bot.run(TOKEN)
'''
