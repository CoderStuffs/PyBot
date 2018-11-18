# Start date November 17th, 2018
# Python v3.6

import json
import discord
from discord.ext import commands

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
        """ Gets called when the client is done preparing the data received from Discord, usually after login. """
        print('Logged in as: ')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def on_message(self, message):
        """ Gets called when there the Bot receives a new message from the server.
            This function handles the logic for responding to various messages and commands.
        """
        if message.author == self.user:
            return

        # If a user types !hello the bot will respond with 'Hello! (nameOfUser here)'.
        if message.content.startswith('!hello'):
            await client.send_message(message.channel, content=(f'Hello! {message.author.mention}')

client = MyClient()
client.run(TOKEN)