from discord.ext import commands
import requests

#API: https://icanhazdadjoke.com
class Joke(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.api = "https://icanhazdadjoke.com"

    @commands.command(brief="pxlbot will make a joke")
    async def joke(self, ctx):
        resp = requests.get("https://icanhazdadjoke.com",
            params={'joke': 'requests+language:python'},
            headers={"Accept":"text/plain"})
        joke = resp.text
        print(f"Response: {resp.text}")
        await ctx.send(joke);


def setup(client):
    client.add_cog(Joke(client))