import os
import discord

from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from discord import Embed
import discord.ext.commands as commands
from discord.ext.commands import Bot as BotBase



#todo: can be removed?
def getSecrets(key):
    return os.environ[key]

CMD_PREFIX = "!"
VERSION = getSecrets('BOT_VERSION')
BOT_TOKEN = getSecrets('BOT_TOKEN')
DEBUG_BOT_CH_ID = int(getSecrets('DEBUG_BOT_CHANNEL_ID'))
GENERAL_CH_ID = int(getSecrets('GENERAL_CHANNEL_ID'))
SERVER_ID = int(getSecrets('SERVER_ID'))
OWNER_ID = int(getSecrets('OWNER_ID'))


def createEmbedIntro():
    embed = Embed(title="Makeway! pxlbot is now online!",
                  description="The great pxlbot is back.",
                  color=0xFF0000,
                  timestamp=datetime.utcnow())
    github_raw_path = "https://raw.githubusercontent.com/kirbysebastian/pxltdphbot/master"
    embed.set_image(url=github_raw_path +
                    "/img/bot/despicable_minions.jpg")
    embed.set_footer(text="Online!")
    return embed

intents = discord.Intents.default()
intents.members = True
pxlbot = commands.Bot(
    command_prefix=commands.when_mentioned_or(CMD_PREFIX),
    intents=intents
)


@pxlbot.event
async def on_ready():
    print("Im ready!")
    channel = pxlbot.get_channel(DEBUG_BOT_CH_ID)
    embed = createEmbedIntro()
    await channel.send(embed=embed)
    await channel.send(content="I'm watching you now! :eyes:\n")


@pxlbot.event
async def on_command_error(ctx, error):
    print(error)


@pxlbot.event
async def on_member_join(member):
    channel = pxlbot.get_channel(DEBUG_BOT_CH_ID)
    print(f"{member.name} has joined the server")
    #todo: create welcome embed
    await channel.send(
        f"Welcome to the club {member.display_name}! Pa-cheese burger ka naman.")
    


@pxlbot.command(hidden=True)
async def load(ctx, extension):

    if (not await ctx.bot.is_owner(ctx.author)):
        print("Unauthorized user")
        return

    print(f"Trying to load: {extension}")    
    msg = f"Successfully loaded: '{extension}'"
    try:
        pxlbot.load_extension(f'src.cogs.{extension}')
    except commands.ExtensionNotFound:
        msg = f"'{extension}' not found."
    except commands.ExtensionAlreadyLoaded:
        msg = f"'{extension}' is already loaded"
    except commands.NoEntryPointError:
        msg = f"'{extension}' doesn't have any setup"
    except commands.ExtensionFailed:
        msg = f"'{extension}' failed to execute"

    print(msg)
    await ctx.send(msg)

@pxlbot.command(hidden=True)
async def unload(ctx, extension):
    if (not await ctx.bot.is_owner(ctx.author)):
        print("Unauthorized user")
        return

    print(f"Trying to unload: {extension}")    
    msg = f"Successfully unloaded: '{extension}'"
    try:
        pxlbot.unload_extension(f'src.cogs.{extension}')
    except commands.ExtensionNotFound:
        msg = f"'{extension}' not found"
    except commands.ExtensionNotLoaded:
        msg = f"'{extension}' is not yet loaded"

    print(msg)
    await ctx.send(msg)

def getBot():
    return pxlbot

def loadAllCommands():
    for fname in os.listdir('src/cogs/'):
        if fname.endswith('.py') and fname != '__init__.py':
            cogname = fname[:-3]
            try:
                pxlbot.load_extension(f'src.cogs.{cogname}')
                print(f"cog.{cogname} has been loaded")
            except commands.ExtensionNotFound:
                print(f"cog.{cogname} not found.")
            except commands.ExtensionAlreadyLoaded:
                print(f"cog.{cogname} is already loaded")
            except commands.NoEntryPointError:
                print(f"cog.{cogname} doesn't have any setup")
            except commands.ExtensionFailed:
                print(f"cog.{cogname} failed to execute")
