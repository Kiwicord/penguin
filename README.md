# Penguin
A python discord bot written in hikari.
## Support
The bot supports only slash commands. Maybe prefix commands in the future.
## Website
Website is coming soon.
## Example
```py
@bot.listen(hikari.GuildMessageCreateEvent)
async def on_message(event):
    if event.content == 'zocker':
        await event.message.respond('Zocker bitte komm wieder zurück :(')
```