import pymorphy2
from discord.ext import commands
from hv import TOKEN


class TranslatorBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        await ctx.send('https://yastatic.net/s3/lyceum/content/images/second-year/chatbot-3/chat-bot-3-4.png - this is help')


    @commands.command(name='alive')
    async def alive(self, ctx, word):
        morph = pymorphy2.MorphAnalyzer()
        zhivoe = morph.parse('Живое')[0]
        p = morph.parse(word)
        word_ = None
        for par in p:
            if 'NOUN' in par.tag:
                word_ = par
                break
        try:
            f = word_.tag.gender
            num = word_.tag.number
            if 'anim' in word_.tag:
                if 'plur' in word_.tag:
                    mes_send = f'{word.capitalize()} {zhivoe.inflect({num}).word}'
                else:
                    mes_send = f'{word.capitalize()} {zhivoe.inflect({f, num}).word}'
            else:
                if 'plur' in word_.tag:
                    mes_send = f'{word.capitalize()} не {zhivoe.inflect({num}).word}'
                else:
                    mes_send = f'{word.capitalize()} не {zhivoe.inflect({f, num}).word}'
        except Exception:
            mes_send = 'Не существительное'
        await ctx.send(mes_send)

    @commands.command(name='morph')
    async def morph(self, ctx, word):
        morph = pymorphy2.MorphAnalyzer()
        mes_send = morph.parse(word)[0].tag.cyr_repr
        await ctx.send(mes_send)

    @commands.command(name='numerals')
    async def numerals(self, ctx, word, num):
        morph = pymorphy2.MorphAnalyzer()
        word_parse = morph.parse(word)[0].make_agree_with_number(int(num)).word
        await ctx.send(f'{num} {word_parse}')

    @commands.command(name='noun')
    async def noun(self, ctx, word, case, number):
        morph = pymorphy2.MorphAnalyzer()
        word_parse = morph.parse(word)[0]
        if 'NOUN' in word_parse[1]:
            mes_send = word_parse.inflect({case})[0] \
                if number == 'single' else \
                word_parse.inflect({case, 'plur'})[0]
        else:
            mes_send = f'{word.capitalize()} не существительное'
        await ctx.send(mes_send)

    @commands.command(name='inf')
    async def infinitive(self, ctx, word):
        morph = pymorphy2.MorphAnalyzer()
        word_parse = morph.parse(word)[0]
        mes_send = word_parse.normal_form
        await ctx.send(mes_send)


bot = commands.Bot(command_prefix='//')
bot.add_cog(TranslatorBot(bot))
bot.run(TOKEN)
bot.run(TOKEN)