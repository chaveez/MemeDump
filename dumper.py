import urllib3
from bs4 import BeautifulSoup
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = 'NTI3NTY4NjY5NzQ0NTYyMTc5.DwWeRA.ZlY1xG6NZqzbhFcdFNpzKDivdbs'

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='dump',
                description="grabs some random memes from worksafe GIF on 4chan",
                brief="dumps some memes",
                aliases=['meme', 'memes'],
                pass_context=True)
async def dump(context):
    url = 'http://boards.4channel.org/wsg/'
    await client.say("If u don't like them go do it yourself, " + context.message.author.mention)


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with memes"))
    print("Logged in as " + client.user.name)


client.run(TOKEN)
