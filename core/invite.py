import hikari
import lightbulb
import datetime
import miru

plugin = lightbulb.Plugin('InvitePlugin')

@plugin.command
@lightbulb.command(name='invite', description='Invite Penguin to your discord server')
@lightbulb.implements(lightbulb.SlashCommand)
async def invite_cmd(ctx):
    embed = (
        hikari.Embed(
            title='Thank you for choosing the best penguin experience',
            color=0xffffff,
            timestamp=datetime.datetime.now().astimezone()
        )
    )

    button = miru.Button(label='Get started', style=hikari.ButtonStyle.LINK, url='https://discord.com/api/oauth2/authorize?client_id=968510806738223154&permissions=8&scope=bot%20applications.commands')
    
    view = miru.View()
    view.add_item(button)

    await ctx.respond(embed, components=view.build())

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)