#!/usr/bin/python3.8

import os
from src.bot import bot

pxlbot = bot.getBot()
bot.loadAllCommands()
pxlbot.run(os.environ["BOT_TOKEN"])

