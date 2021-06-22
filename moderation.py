from discord import User
from discord.ext import commands
from discord_slash import cog_ext
class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def ban(self, ctx, member: User):
        await ctx.guild.ban(member)
    
    @commands.command(name="ban")
    async def ban_normal(self, ctx, member: User):
        await self.ban(ctx, member)
    
    @cog_ext.cog_slash(name="ban")
    async def ban_slash(self, ctx, member: User):
        await self.ban(ctx, member)