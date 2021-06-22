from discord.ext.commands import Bot
from dotenv import load_dotenv
from os import environ

load_dotenv()

bot = Bot()

bot.run(environ['WARP_TOKEN'])