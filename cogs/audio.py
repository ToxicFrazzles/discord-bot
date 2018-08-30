import discord
from discord.ext import commands
import asyncio
import os
from time import sleep
import json

class Audio:
	"""Some audio commands"""
	def __init__(self,bot):
		self.bot=bot
		self.settings_file = "data/Audio/settings.json"
		try:
			with open(self.settings_file) as f:
				self.settings = json.load(f)
		except FileNotFoundError:
			self.settings = {}
			with open(self.settings_file,"w") as f:
				json.dump(self.settings,f)
		except json.JSONDecodeError:
			print("Error in the json file",self.settings_file,"erasing it and starting again")
			self.settings = {}
			with open(self.settings_file,"w") as f:
				json.dump(self.settings,f)
	
	def save_settings(self):
		with open(self.settings_file,"w") as f:
			json.dump(self.settings,f)
	
	@commands.group()
	async def audioset(self,ctx):
		if not ctx.invoked_subcommand:
			await ctx.send("This command only has subcommands and I don't know how to show you the help here")
	
	@audioset.command()
	async def volume(self,ctx,volume:int):
		if volume > 200:
			volume = 200
		elif volume < 0:
			volume = 0
		self.settings[str(ctx.guild.id)] = {}
		self.settings[str(ctx.guild.id)]['volume'] = volume
		self.save_settings()
		await ctx.send("Volume is now set to "+str(volume)+"%")


def check_folders():
	folders = ["data/Audio"]
	for folder in folders:
		if os.path.exists(folder) and os.path.isdir(folder):
			continue
		else:
			print("Created folder",folder)
			os.makedirs(folder)

def setup(bot):
	check_folders()
	n = Audio(bot)
	bot.add_cog(n)