# Work with Python 3.6 and rewrite discord.py
import discord
import asyncio
from discord.ext import commands

TOKEN = 'NTE0MDEwMDk4Mjc3MDIzNzQ0.DtQVAA.tOBJPqLxMhrgZdvrVd6UVJfJ0sg'
LAUNDRY_TIMER = 45
prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command(pass_context=True)
async def stopit(ctx, member: discord.Member):
    await ctx.send("stop that " + member.mention + " or i'm gonna be the next one to rape you :wave: :eggplant:")

@bot.command(pass_context=True)
async def laundryMachine(channel, member: discord.Member):
    await bot.send_message(channel, "You just started the laundry machine, it will be ready in " + str(LAUNDRY_TIMER) + "minuts")
    await channel.send("you will be notified when this one will be over, at the meantime, you can go fap ! :wave:")
    await asyncio.sleep(10)
    await channel.send("Hey, your laundry machine just finished, go check it out and take everything off !")
    await channel.send("Don't forget your socks at the bottom ! :smiley:")

bot.run(TOKEN)  # Where 'TOKEN' is your bot token