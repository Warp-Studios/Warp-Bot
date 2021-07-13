from discord.ext.commands import Bot, when_mentioned_or
from dotenv import load_dotenv
from os import environ
from discord_slash import SlashCommand

load_dotenv()

bot = Bot(command_prefix=when_mentioned_or('warp.'))
slash = SlashCommand(bot, sync_commands=True)

bot.load_extension("moderation")
bot.load_extension("fun")


bot.run(environ['WARP_TOKEN'])