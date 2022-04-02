#!/usr/bin/python3.8

from src.bot import bot

pxltdbot = bot.AdminBot()

@pxltdbot.command()
async def load(ctx, extension):
    pxltdbot.load_extension(f'cogs.{extension}')
    await ctx.send("Loading...")

@pxltdbot.command()
async def unload(ctx, extension):
    pxltdbot.unload_extension(f'cogs.{extension}')
    await ctx.send("Unloading...")

pxltdbot.run()

