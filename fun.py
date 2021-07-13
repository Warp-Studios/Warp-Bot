from discord.ext import commands
from discord_slash import cog_ext

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def bonk(self, ctx):
        ctx.send("bonk")     
    
    @commands.command(name='bonk')
    def bonk_normal(self, ctx):
        self.bonk(ctx)
    
    @cog_ext.cog_slash(name="bonk")
    def bonk_slash(self, ctx):
        self.bonk(ctx)

def setup(bot):
    bot.add_cog(Fun(bot))