import discord
from discord.ext import commands
import asyncio
import random
import os

bot = commands.AutoShardedBot(command_prefix='/')

@bot.event
async def on_ready():
	print('Logged in as',bot.user.name)
	print('-'*10)
	await bot.change_presence(activity=discord.Activity(name="The Grim Adventures of Billy and Mandy",type=discord.ActivityType.watching))

@bot.command()
async def roll(ctx,dice:str):
	"""Rolls dice in NdN format"""
	try:
		rolls,limit = map(int, dice.split('d'))
	except Exception:
		await ctx.send('Format has to be NdN!')
		return
	result = ', '.join(str(random.randint(1,limit)) for r in range(rolls))
	await ctx.send(result)

@bot.command()
async def play(ctx,ptype:str,*,game:str):
	"""Sets the game being played"""
	if ptype == "playing":
		actype = discord.ActivityType.playing
	elif ptype == "streaming":
		actype = discord.ActivityType.streaming
	elif ptype == "listening":
		ptype = "listening to"
		actype = discord.ActivityType.listening
	elif ptype == "watching":
		actype = discord.ActivityType.watching
	else:
		await ctx.send("Usage: `/play <type> <name>` where type is one of playing, streaming, listening and watching")
		return
	await bot.change_presence(activity=discord.Activity(name=game,type=actype))
	await ctx.send("Now {} {}".format(ptype,game))

if __name__=="__main__":
	try:
		with open("token.txt","r") as f:
			token = f.read().rstrip()
	except FileNotFoundError:
		token = input("Client token: ")
		with open("token.txt","w") as f:
			f.write(token)
	bot.run(token)
