from json import dump
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

client = commands.Bot(command_prefix = "!")
async def test1(): 

    checkaddr = db1.geta()#  second addreses
    print(db1.geta())
    checkaddr1 = list(checkaddr.values())
    print(checkaddr1)
    for element in checkaddr1:
        print('check' + element)
        json = await tools.getonl(element)
        if json == False:
            author = int(db.get(element))
            owner = await client.fetch_user(author)  # your user ID
            await owner.send("YOUR NODE IS NOT ONLINE!")    
async def check(): 
    while True:
        checkaddr = db1.geta()#  second addreses
        print(db1.geta())
        checkaddr1 = list(checkaddr.values())
        print(checkaddr1)
        for element in checkaddr1:
            print('check' + element)
            json = await tools.getonl(element)
            if json == False:
                author = int(db.get(element))
                owner = await client.fetch_user(author)  # your user ID
                if len(client.cached_messages):
                    await owner.send("YOUR NODE IS NOT ONLINE!")   

        await asyncio.sleep(600)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name="`!cmds` for help!"))
    await check()

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
    else:
        await ctx.send('INVALID COMMAND')
@client.command()
async def test(ctx):
      await test1()

@client.command()
async def cmds(ctx):
    await ctx.send('---Help--')
    await ctx.send('1. !watch <address> # Add address to watch')
    await ctx.send('2. !delite <address> <number> # You will get number when you add watch address')




 


client.run('ODYxOTAyMDA3NjM0NDkzNDUw.YOQiyw.YN8sxlLQvZL-SVuyFvxlKDXEz7o')