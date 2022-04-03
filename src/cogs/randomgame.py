import random
from discord.ext import commands

class RandomGame(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.games = []

    @commands.command(brief="Choose a random game for you")
    async def randomgame(self, ctx):
        if len(self.games) == 0:
            await ctx.send(f"No available games added. Run `!addgame`");
            return
            
        await ctx.send(f"You should play '{random.choice(self.games)}'");


    @commands.command(brief="Add a game choice to `!randomgame`")
    async def addgame(self, ctx, game: str):
        msg = f"{game} is added to `!randomgame`"
        self.games.append(game);
        print(msg)
        await ctx.send(msg)


    @commands.command(brief="Remove a game choice from `!randomgame`")
    async def removegame(self, ctx, game: str):
        msg = f"{game} is removed from `!randomgame`"
        self.games.remove(game);
        print(msg)
        await ctx.send(msg)

    
    @commands.command(brief="Shows the list of games added to `!randomgame`")
    async def showgames(self, ctx):
        if len(self.games) == 0:
            await ctx.send(f"No available games added. Run `!addgame`");
            return
        
        print(self.games)
        await ctx.send(self.games)
        

    @commands.command(brief="Shows the list of games added to `!randomgame`")
    async def deleteallgames(self, ctx):      
        self.games.clear()
        msg = "All games from `!randomgame` has been removed"
        print(msg)
        await ctx.send(msg)

def setup(client):
    client.add_cog(RandomGame(client))