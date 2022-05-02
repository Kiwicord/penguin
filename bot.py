import hikari
import lightbulb
import miru

from os import getenv
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(
    token=getenv('TOKEN'),
    prefix=lightbulb.when_mentioned_or('-'), # idk why i put that here if the bot only uses slash cmds but hey
    default_enabled_guilds=(958713468624728114, 946054793921699860),
)

miru.load(bot)

bot.load_extensions_from('core')
bot.run()