# Start date November 17th, 2018
# Python v3.6

import json
import discord
from discord.ext import commands
from datetime import datetime, timedelta

cacheJSON = 'json/cache.json'

with open(cacheJSON, 'r') as jfile:
    contents = json.load(jfile)
    TOKEN = contents['token']

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    async def on_message(self, message):
        if message.author.bot or message.author == self.user:
            return
        
        await self.process_commands(message)
    
    def getGuild(self):
        return self.guilds[0]
    
    def getTextChannels(self):
        guild = self.getGuild()
        return guild.text_channels
    

bot = Bot(command_prefix='!', case_insensitive=True)

def notpinned (msg):
    """Check if the message is pinned."""
    return msg.pinned == False

"""
BOT 
EVENTS
"""

@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

"""
BOT 
COMMANDS
"""

@bot.command()
async def hello(ctx):
    """If a user types !hello the bot will respond with 'Hello! (nameOfUser here)'."""
    
    await ctx.send(f"Hello! {ctx.author.mention}")

@bot.command()
async def cleanhere(ctx):
    """When an admin types !cleanhere the bot will delete all old messages (from more than five days ago) in that channel. """
    channel = ctx.channel
    
    now = datetime.now()
    bfr = now - timedelta(days=5)
    deleted = await channel.purge(limit=5000, check=notpinned, before=bfr)
    await channel.send(f"Cleaned up this channel, deleted {len(deleted)} messages.")

@bot.command()
async def cleanall():
    """When an admin types !cleanall the bot will delete all old messages (from more than five days ago) in that channel. """
    channels = bot.getTextChannels()
    exceptedCategories = ["Admin", "README.md"]

    now = datetime.now()
    bfr = now - timedelta(days=5)
    for channel in channels:
        deleted = []
        if channel.category.name not in exceptedCategories:
            deleted = await channel.purge(limit=5000, check=notpinned, before=bfr)
            await channel.send(f"Cleaned up this channel, deleted {len(deleted)} messages.")

bot.run(TOKEN)

