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
async def play(game:str):
	"""Sets the game being played"""
	await bot.change_presence(game=discord.Game(name=game))

if __name__=="__main__":
	try:
		with open("token.txt","r") as f:
			token = f.read().rstrip()
	except FileNotFoundError:
		token = input("Client token: ")
		with open("token.txt","w") as f:
			f.write(token)
	bot.run(token)
