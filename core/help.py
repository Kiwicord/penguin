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
            miru.SelectOption(label='Music', emoji='🎶'),
            miru.SelectOption(label='Moderation', emoji='🔧'),
            miru.SelectOption(label='Economy', emoji='💰')
        ]
    )
    async def help_select(self, select_menu, ctx):
        value = select_menu.values[0]

        if value == 'Moderation':
            moderation_embed = (
                hikari.Embed(
                    title='Moderation Commands',
                    description='Mod commands LOL',
                    color=0xffffff
                )
            )

            dm_channel = await ctx.author.fetch_dm_channel()
            await dm_channel.send(moderation_embed)

@plugin.listener(hikari.GuildMessageCreateEvent)
async def help_cmd(event):
    if event.is_bot or not event.content:
        return

    if event.content == 'allah':
        embed = (
            hikari.Embed(
                title='Bot Commands',
                description='Click any button to get all the commands of a topic.',
                color=0xffffff,
                timestamp=datetime.datetime.now().astimezone()
            )
            .set_footer(f'Requested by {event.message.author}')
        )

        view = HelpView()

        msg = await event.message.respond(embed, components=view.build())

        view.start(message=msg)
        await view.wait()
        await event.message.respond('view timed out loil')

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)