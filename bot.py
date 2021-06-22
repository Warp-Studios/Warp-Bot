from discord.ext.commands import Bot
from dotenv import load_dotenv
from os import environ

load_dotenv()

bot = Bot()

bot.run(os.environ['WARP_TOKEN'])