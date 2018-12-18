import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

Client = discord.Client()
bot = commands.Bot(command_prefix="!")
lines = open(r'(TXT hier)').read().splitlines()

@bot.event
async def on_ready():
    print("The bot is online!")

@bot.command(pass_context=True)
async def fitbit(ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        await bot.delete_message(ctx.message)
    myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="FitBit account!", color=0xf45eff)
    embed.add_field(name="Email:", value=split[0], inline=False)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

    print("{} Typed !Spotify".format(userName))

bot.run("5Apjy3QsoHcj_RKzaGQ6mnPioJfDuU5n")
