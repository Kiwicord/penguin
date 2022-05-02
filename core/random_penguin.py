import hikari
import lightbulb
import datetime
import random

from os import getenv
from dotenv import load_dotenv
from pexels_api import API

load_dotenv()

plugin = lightbulb.Plugin(name='RandomPenguin')
api = API(getenv('API_KEY'))

@plugin.command()
@lightbulb.command(name='penguin', description='Sends a random penguin image.')
@lightbulb.implements(lightbulb.SlashCommand)
async def random_penguin(ctx):
    api.search('penguin', page=1, results_per_page=70)
    photos = api.get_entries()

    penguin = random.choice(photos)

    embed = (
        hikari.Embed(
            title='🐧🐧🐧🐧🐧',
            color=0xffffff,
            timestamp=datetime.datetime.now().astimezone()
        )
        .set_image(penguin.original)
        .set_footer(f'Requested by {ctx.author  }')
    )

    await ctx.respond(embed)

def load(bot):
    bot.add_plugin(plugin)


def unload(bot):
    bot.remove_plugin(plugin)