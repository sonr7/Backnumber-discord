import discord
import asyncio
import os

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('大不正解')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('#back number:'):
        kasi = message.content.replace('#back number:')
        back number:', '')
        with open(kasi) as kasii:
            kasiyaru = kasii.read()
        await message.channel.send(kasiyaru)

client.run(token)
