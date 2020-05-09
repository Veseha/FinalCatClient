import pymorphy2
from discord.ext import commands
import discord
import random
import requests
from hv import TOKEN

urlya = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class TranslatorBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.lang = 'en-ru'

    @commands.command(name='set_lang')
    async def set_lang(self, ctx, lang):
        self.lang = lang
        await ctx.send('ok')

    @commands.command(name='help_bot')
    async def help(self, ctx):
        message = '// comand text'
        await ctx.send(message)

    @commands.command(name='text')
    async def translate(self, ctx, *text):
        par = {
            'key': 'iam not have a token потму что я ленивый, но это долэно работать',
            'lang': self.lang,
            'text': ' '.join(text)
        }
        response = requests.get(urlya, params=par).json()
        await ctx.send(' '.join(response['text']))


bot = commands.Bot(command_prefix='//')
bot.add_cog(TranslatorBot(bot))
bot.run(TOKEN)