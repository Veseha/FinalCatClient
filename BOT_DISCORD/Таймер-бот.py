import discord
import requests
from hv import TOKEN
import datetime
client = discord.Client()
h, m, flag, time, whatch = 0, 0, False, None, '⏰'


@client.event
async def on_message(message):
    global h, m, flag, time
    if message.author == client.user:
        return
    if 'set_timer' in message.content.lower():
        h = int(message.content.split('in ')[1].split(' hours')[0])
        m = int(message.content.split('hours ')[1].split(' min')[0])
        flag = True
        time = datetime.datetime.now()
        await message.channel.send(f'The timer should start in {h} hours and {m} min.')
    if flag:
        while True:
            delta = datetime.datetime.now() - time
            if delta.seconds >= h * 3600 + m * 60:
                h, m, flag, time = 0, 0, False, None
                break
        await message.channel.send(f'{whatch} Time X has come!')


client.run(TOKEN)
client.run(TOKEN)