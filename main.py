import discord
from discord.ext import commands
import asyncio
import random
import os

bot = commands.AutoShardedBot(command_prefix='/')
persistent_cogs = ["owner"]

@bot.event
async def on_ready():
	print('Logged in as',bot.user.name)
	print('-'*10)
	acname = "The Grim Adventures of Billy and Mandy"
	actype = discord.ActivityType.watching
	await bot.change_presence(activity=discord.Activity(name=acname,type=actype))



if __name__=="__main__":
	try:
		with open("token.txt","r") as f:
			token = f.read().rstrip()
	except FileNotFoundError:
		token = input("Client token: ")
		with open("token.txt","w") as f:
			f.write(token)
	for cog in persistent_cogs:
		try:
			bot.load_extension("cogs."+cog)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__,e)
			print('Failed to load extension {}\n{}'.format(cog, exc))
	bot.run(token)
