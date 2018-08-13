import discord
from discord.ext import commands
import asyncio
import os
import datetime

class General:
	"""Some generic commands"""
	def __init__(self,bot):
		self.bot = bot
	
	@commands.command(name="ping")
	async def ping(self,ctx):
		"""pong"""
		sent = ctx.message.created_at
		diff = datetime.datetime.now() - sent
		milliseconds = diff.microseconds/1000
		await ctx.send("pong {:.2f}ms".format(milliseconds))
	
	@commands.command(name="say")
	async def say(self,ctx,*,message:str):
		await ctx.send(message)
	
	@commands.command(name="invite")
	async def invite(self,ctx):
		info = await self.bot.application_info()
		link = "https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8".format(info.id)
		await ctx.send("Just click this link to invite me to your server: {}".format(link))
	

def check_folders():
	folders = []
	for folder in folders:
		if os.path.exists(folder) and os.isdir(folder):
			continue
		else:
			print("Created folder",folder)
			os.makedirs(folder)

def setup(bot):
	check_folders()
	n = General(bot)
	bot.add_cog(n)
