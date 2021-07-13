from discord.ext import commands
from discord_slash import cog_ext

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def bonk(self, ctx):
        await ctx.send("bonk")     
    
    @commands.command(name='bonk')
    async def bonk_normal(self, ctx):
        await self.bonk(ctx)
    
    @cog_ext.cog_slash(name="bonk")
    async def bonk_slash(self, ctx):
        await self.bonk(ctx)

def setup(bot):
    bot.add_cog(Fun(bot))