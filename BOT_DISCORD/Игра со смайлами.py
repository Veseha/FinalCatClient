import pymorphy2
from discord.ext import commands
import discord
import random
from hv import TOKEN
emoji = [':middle_finger:', ':joy:', ':thinking:', ':floppy_disk:', ':slight_smile:']
score = {'user': 0, 'bot': 0}

client = discord.Client()


@client.event
async def on_message(message):
    random.shuffle(emoji)
    if message.author == client.user:
        return
    if message.content == '/help' or message.content == '/start':
        await message.channel.send(f'input int and i write smile, no rules')
    elif message.content == '/stop':
        score['user'] = 0
        score['bot'] = 0
        await message.channel.send('Buy!')
    else:
        try:
            if emoji:
                user = emoji.pop(int(message.content) % len(emoji))
                bot = emoji.pop(random.randint(0, 100) % len(emoji))
                if user > bot:
                    score['user'] += 1
                else:
                    score['bot'] += 1
                await message.channel.send(f'Your smile {user}\nBot smile {bot}\nScore: You {score["user"]} '
                                           f'- Bot {score["bot"]}')
        except IndexError:
            if score["user"] > score["bot"]:
                await message.channel.send(f'Score: You {score["user"]} - Bot {score["bot"]}\nYou win...')
            elif score["user"] < score["bot"]:
                await message.channel.send(f'Score: You {score["user"]} - Bot {score["bot"]}\nBot win')
            else:
                await message.channel.send(f'Score: You {score["user"]} - Bot {score["bot"]}\nfriends!')
        except Exception as e:
            print(e, message.content)
            await message.channel.send('err')


client.run(TOKEN)