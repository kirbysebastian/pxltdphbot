import os
import discord

from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from discord import Embed
from discord.ext.commands import Bot as BotBase

PREFIX = "!" #CommandPrefix

class AdminBot(BotBase):
    def __init__(self):
        self.ready = False
        self.PREFIX = PREFIX
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        self.TOKEN = self.getSecrets('TOKEN')
        self.DEBUG_BOT_CH_ID = int(self.getSecrets('DEBUG_BOT_CHANNEL_ID'))
        self.SERVER_ID = int(self.getSecrets('SERVER_ID'))
        self.OWNER_ID = int(self.getSecrets('OWNER_ID'))

        super().__init__(command_prefix=PREFIX, owner_ids=[self.OWNER_ID])


    def run(self, version):
        self.VERSION = version
        print("AdminBot is running...")
        super().run(self.TOKEN, reconnect=True)

    
    def getSecrets(self, key):
        return os.environ[key]

    
    def get_embed_intro(self):
        embed = Embed(title="Makeway! pxlbot is now online!",
                      description="The great pxlbot is now back!",
                      color=0xFF0000,
                      timestamp=datetime.utcnow())
        embed.set_author(name="pxltdbot", icon_url=self.guild.icon_url)
        github_raw_path = "https://raw.githubusercontent.com/kirbysebastian/pxltdphbot/master"
        embed.set_thumbnail(
            url=github_raw_path+"/img/bot/clown_bot_embed_intro.jpg")
        embed.set_image(url=github_raw_path+"/img/bot/despicable_minions.jpg")
        embed.set_footer(text="Behold!")

        return embed
        

    async def on_connect(self):
        print("AdminBot Connected.")


    async def on_disconnect(self):
        print("AdminBot Disconnected.")


    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(self.SERVER_ID)
            print("AdminBot is ready.")
        else:
            print("AdminBot reconnected.")

        channel = self.get_channel(self.DEBUG_BOT_CH_ID)
        embed = self.get_embed_intro()
        await channel.send(content="Watsup bitches?! I'm now online 3:)", embed=embed)


    async def on_message(self, message):
        pass

