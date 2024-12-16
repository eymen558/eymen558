import discord

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTMxODIyNzY2NDkwMDg1Mzc2MA.GTeRmH.U9R7Y3KkdNnhJhWbdJ0Pv_cf-9bb9JHB9z6MJk")


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
