import hikari
import lightbulb
from os import getenv
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(
    token=getenv('TOKEN'),
    prefix='-',
    default_enabled_guilds=(958713468624728114)
)

@bot.listen(hikari.StartedEvent)
async def started(event):
    print('bot has started')

bot.run()