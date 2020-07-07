from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "!" #CommandPrefix
CH_ID_PATH = "../channels/ids.txt"
TOKEN_PATH = "./../channels/token"

class AdminBot(BotBase):
    def __init__(self):
        self.ready = False
        self.PREFIX = PREFIX
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        self.CHANNEL_IDS = self.get_channel_ids()

        super().__init__(command_prefix=PREFIX, owner_ids=[self.CHANNEL_IDS["OWNER"]])


    def run(self, version):
        self.VERSION = version

        with open(TOKEN_PATH, "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        super().run(self.TOKEN, reconnect=True)
        print("AdminBot is running...")

    def get_channel_ids(self):
        with open(CH_ID_PATH, 'r') as f:
            ids = [data for data in f.read().split('\n')]
            ids.remove('')
            channel_ids = {s.split("=")[0]:int(s.split("=")[1]) for s in ids}
            return channel_ids

    async def on_connect(self):
        print("AdminBot Connected.")


    async def on_disconnect(self):
        print("AdminBot Disconnected.")


    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(self.CHANNEL_IDS["SERVER"])
            print("AdminBot is ready.")
        else:
            print("AdminBot reconnected.")

        DEBUG_BOT = self.CHANNEL_IDS["DEBUG_BOT"]
        channel = self.get_channel(DEBUG_BOT)
        await channel.send("Watsup?! I'm now online and happy to serve you! :)")


    async def on_message(self, message):
        pass

