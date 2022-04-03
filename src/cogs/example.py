from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief="Just a dummy command")
    async def ping(self, ctx):
        await ctx.send("Heya!");

def setup(client):
    client.add_cog(Example(client))