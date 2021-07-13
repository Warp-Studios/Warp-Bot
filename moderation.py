from discord import User
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
from bot import slash
from discord_slash import SlashContext

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def ban(self, ctx, member: User):
        if type(ctx) == type(SlashContext):
            if ctx.author.guild_permissions.ban_members:
                await ctx.guild.ban(member)
                await ctx.send("Banned {}".format(member), hidden=True)
            else:
                await ctx.send("You do not have permission to ban members", hidden=True)       
        if ctx.author.guild_permissions.ban_members:
            await ctx.guild.ban(member)
            await ctx.send("Banned {}".format(member), hidden=True)
        else:
            await ctx.send("You do not have permission to ban members", hidden=True)       
    @commands.command(name="ban", category="Moderation")
    async def ban_normal(self, ctx, member: User):
        await self.ban(ctx, member)
    @cog_ext.cog_slash(name="ban", guild_ids=[842948029245161492])
    async def ban_slash(self, ctx, member: User):
        await self.ban(ctx, member)

def setup(bot):
    bot.add_cog(Moderation(bot))