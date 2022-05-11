import hikari
import lightbulb
import miru
import datetime

plugin = lightbulb.Plugin('HelpCommand')

class HelpView(miru.View):
    @miru.select(
        placeholder='Select topic',
        options=[
            miru.SelectOption(label='Fun', emoji='🧩'),
            # miru.SelectOption(label='Music', emoji='🎶'),
            # miru.SelectOption(label='Moderation', emoji='🔧'),
            # miru.SelectOption(label='Economy', emoji='💰')
        ]
    )
    async def help_select(self, select_menu, ctx):
        value = select_menu.values[0]
        
        if value == 'Fun':
            fun_embed = (
                hikari.Embed(
                    title='🧩 Fun Commands',
                    color=0xffffff
                )
                .add_field(name='/penguin', value='Sends a random image of a penguin')
            )
            dm_channel = await ctx.user.fetch_dm_channel()
            await dm_channel.send(fun_embed)

@plugin.command
@lightbulb.command('help', 'Sends bot help')
@lightbulb.implements(lightbulb.SlashCommand)
async def help_cmd(ctx):
    embed = (
        hikari.Embed(
            title='Bot Commands',
            description='Click any button to get all the commands of a topic.',
            color=0xffffff,
            timestamp=datetime.datetime.now().astimezone()
        )
        .set_footer(f'Requested by {ctx.author}')
    )
    view = HelpView()
    msg = await ctx.respond(embed, components=view.build())
    view.start(message=await msg.message())
    await view.wait()
    await ctx.respond('view timed out loil')

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)