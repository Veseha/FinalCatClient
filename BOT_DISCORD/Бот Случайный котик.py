import discord
import requests
from hv import TOKEN
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "кот" in message.content.lower():
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        data = response.json()
        await message.channel.send(data[0]['url'])
    if "собак" in message.content.lower():
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        data = response.json()
        await message.channel.send(data['message'])


client.run(TOKEN)