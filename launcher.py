#!/usr/bin/python3.8

import os
from lib.bot import bot

pxltdbot = bot.AdminBot()
pxltdbot.run(os.environ['BOT_VERSION'])

