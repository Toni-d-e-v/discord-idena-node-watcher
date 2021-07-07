from json import dump
from typing import ChainMap
from discord.ext.commands.core import check
import tools
import discord
from discord.ext import commands
from db import DB
import time
from discord.utils import get
from threading import Thread
import asyncio
import schedule

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
db = DB("db/addrtouser.db")
db1 = DB("db/addrstorage.db")
db2 = DB("db/number.db")
db3 = DB("db/calluser.db")

client = commands.Bot(command_prefix = "!")

async def check(): 

    while True:
        checkaddr = db1.geta()#  second addreses
        print(db1.geta())
        checkaddr1 = list(checkaddr.values())
        print('All addresses users:',checkaddr1)
        checkuser = db3.geta()#  second addreses
        print(db3.geta())
        checkuserr1 = list(checkuser.values())
        print('All called users:',checkuserr1)

        how = db2.get("how")

        for element in checkaddr1:
            print('check' + element)
            json = await tools.getonl(element)
            if json == False:
                print(element+',is ofline')

                author = int(db.get(element))
                owner = await client.fetch_user(author)  # your user ID
                if author not in checkuserr1:
                    await owner.send("YOUR NODE IS NOT ONLINE!,"+element)
                    db3.set(how,author) #Sets Value
   

        await asyncio.sleep(900)

async def check1(): 
    while True:
        print('all users delited from calluser.db')
        db3.resetdb()#  second addreses
        await asyncio.sleep(3600)

async def main():
    while True:
        await check()
        await check1()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name="`!cmds` for help!"))
    loop = asyncio.get_event_loop()
    loop.create_task(check())
    loop.create_task(check1())


@client.command()
async def watch(ctx, arg):
    message = str(ctx.message.content)
    author = str(ctx.message.author.id)

    print(message,'User:'+author)
    if '0x' in message:
            how = db2.get("how")
            number = how + 1

            await ctx.send('Now watching:'+ arg)
            await ctx.send('Remove number:'+ str(number))

            db.set(arg , author) #Sets Value

            db1.set(number,arg) #Sets Value
            db2.set('how',number) #Sets Value

    else:
        await ctx.send('Invalid address:'+ arg)
@client.command()
async def delite(ctx, arg, arg1):
    message = str(ctx.message.content)
    author = str(ctx.message.author.id)
    how = db2.get("how")

    print(message,'User:'+author)
    if '0x' in message:
        if author == db.get(arg):
            db.delete(arg) #Sets Value
            db1.delete(arg1) #Sets 
            number = how - 1
            db2.set('how',number) #Sets Value
            await ctx.send('Not watching:'+ arg)

    else:
        await ctx.send('INVALID ADDRESS:'+ arg)
@client.command()
async def reset(ctx):
    author = str(ctx.message.author)
    if author == 'Toni.Dev#6969':
        db.resetdb()
        db1.resetdb()
        db2.resetdb()
        db3.resetdb()

    else:
        await ctx.send('INVALID COMMAND')
@client.command()
async def test(ctx):
    author = str(ctx.message.author.id)   
    how = db2.get("how")
     
    db3.set(how,author) #Sets Value
@client.command()
async def test1(ctx):
    await check1()
     
@client.command()
async def cmds(ctx):
    await ctx.send('---Help--')
    await ctx.send('1. !watch <address> # Add address to watch')
    await ctx.send('2. !delite <address> <number> # You will get number when you add watch address')




 


client.run('your bot token')