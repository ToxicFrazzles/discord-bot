import discord
from discord.ext import commands
import asyncio
import random
import os
from time import sleep
import json

bot = commands.AutoShardedBot(command_prefix='/')
persistent_cogs = ["owner"]

@bot.event
async def on_ready():
	print('Logged in as',bot.user.name)
	print('-'*10)
	acname = "The Grim Adventures of Billy and Mandy"
	actype = discord.ActivityType.watching
	activity = discord.Activity(name=acname,type=actype)
	await bot.change_presence(activity=activity)



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
	try:
		with open("data/Owner/settings.json") as f:
			owner_settings = json.load(f)
		cogs = owner_settings['cogs']
		for cog in cogs:
			bot.load_extension("cogs."+cog)
	except FileNotFoundError:
		pass
	except Exception as e:
		print("Failed to load some of the cogs that were last used")
		print(type(e),str(e))
	bot.run(token,bot=True,reconnect=True)
