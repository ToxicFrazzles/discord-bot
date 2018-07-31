import discord
from discord.ext import commands
import asyncio
import random
import os

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
	print('Logged in as',bot.user.name)
	print('-'*10)
	await bot.change_presence(game=discord.Game(name="Meh",type=2))

@bot.command()
async def roll(dice:str):
	"""Rolls dice in NdN format"""
	try:
		rolls,limit = map(int, dice.split('d'))
	except Exception:
		await bot.say('Format has to be NdN!')
		return
	result = ', '.join(str(random.randint(1,limit)) for r in range(rolls))
	await bot.say(result)

@bot.command()
async def play(ptype:str,game:str):
	"""Sets the game being played"""
	if ptype == "playing":
		pint = 0
	elif ptype == "streaming":
		pint = 1
	elif ptype == "listening":
		ptype = "listening to"
		pint = 2
	elif ptype == "watching":
		pint = 3
	else:
		await bot.say("Usage: `/play <type> <name>` where type is one of playing, streaming, listening and watching")
		return
	await bot.change_presence(game=discord.Game(name=game,type=pint))
	await bot.say("Now {} {}".format(ptype,game))

if __name__=="__main__":
	try:
		with open("token.txt","r") as f:
			token = f.read().rstrip()
	except FileNotFoundError:
		token = input("Client token: ")
		with open("token.txt","w") as f:
			f.write(token)
	bot.run(token)
