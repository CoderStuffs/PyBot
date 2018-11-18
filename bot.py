# Start date November 17th, 2018
# Python v3.6

import json
import discord
from discord.ext import commands
from resources import get_dictionary, search_dictionary

# Ignore the following commented out code. Mods are discussing how we will handle hosting and the bot's token.

# cacheJSON = 'json/cache.json'

# try:
#     with open(cacheJSON, 'r') as foo:
#         contents = json.load(foo)
#         TOKEN = contents['token']

# except FileNotFoundError:
#     pass

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as: ')
        print(self.user.name)
        print(self.user.id)
        print('------')

    # If a user types !hello the bot will respond with 'Hello! (nameOfUser here)'
    async def on_message(self, message):

        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await client.send_message(message.channel, content = (f'Hello! {message.author.mention}')

    @bot.command()
    asynd def info(ctx):


client = MyClient()
client.run(TOKEN)
