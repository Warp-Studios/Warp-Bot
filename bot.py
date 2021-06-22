from discord.ext.commands import Bot
from dotenv import load_dotenv
from os import environ
from discord_slash import SlashCommand

load_dotenv()

bot = Bot()
slash = SlashCommand(bot, sync_commands=True)

bot.run(environ['WARP_TOKEN'])