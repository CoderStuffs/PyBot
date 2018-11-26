# Start date November 17th, 2018
# Python v3.6

from discord.ext import commands
from resources import Resources
# Ignore the following commented out code. Mods are discussing how we will handle hosting and the bot's token.

# cacheJSON = 'json/cache.json'

# try:
#     with open(cacheJSON, 'r') as foo:
#         contents = json.load(foo)
#         TOKEN = contents['token']

# except FileNotFoundError:
#     pass



bot = commands.Bot(command_prefix='!')
resources = Resources()


@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command()
async def hello(ctx: "Context"):
    """
    If a user types !hello the bot will respond with 'Hello! (nameOfUser here)
    """
    await ctx.send(f"Hello! {ctx.message.author.mention}")


def check_info_reaction(reaction, user):
    # return user == message.author and str(reaction.emoji) == '📚'
    return user.id != bot.user.id and str(reaction.emoji) == '📚'

@bot.command()
async def info(ctx: "Contxt"):
    fields = ctx.message.content.split()
    if len(fields) == 1:
        # user only said !info or no spaces "!infopython" and will not work
        await ctx.send(resources.get_help_text())

    else:
        if fields[1] == "add":
            # Possible change - Making sure user has permission to add urls to resource list
            if len(fields) != 4:
                # Not correct number of parameters
                await ctx.send(resources.get_help_text())
                return
            if not resources.add_url(fields[2], fields[3]):
                # add_url wasn't able to confirm that url was in the right format
                await ctx.message.add_reaction('😡')
                return
            await ctx.message.add_reaction('😍')
        else:
            topic = fields[1]
            msg_topic = f"Here are some resources for {topic}\n\n"
            try:
                urls = resources.get_urls(topic)
                msg = '\n'.join([f"<{u}>" for u in resources.get_urls(topic)[:5]])
                msg += "\nReact to this message to get the full list Private Message'd to you!"
                bot_message = await ctx.send(msg_topic + msg)

                # Add reaction and wait for any other reaction
                await bot_message.add_reaction('📚')
                react, user = await bot.wait_for('reaction_add', timeout=60.0, check=check_info_reaction)
                await user.send(msg_topic + '\n'.join([f"<{u}>" for u in resources.get_urls(topic)]))
            except KeyError:
                await ctx.send(resources.get_invalid_text())

bot.run(TOKEN)

