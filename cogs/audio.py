import discord
from discord.ext import commands
import asyncio
import os
from time import sleep

class Audio:
	"""Some audio commands"""
	def __init__(bot):
		self.bot=bot
		self.settings_file = "data/Audio/settings.json"
		try:
			with open(self.settings_file) as f:
				self.settings = json.load(f)
		except FileNotFoundError:
			self.settings = {}
			with open(self.settings_file,"w") as f:
				json.dump(self.settings,f)
	
	def save_settings(self):
		with open(self.settings_file,"w") as f:
			json.dump(self.settings,f)
	
	@commands.group()
	async def audioset(ctx):
		if not ctx.invoked_subcommand:
			await ctx.send("This command only has subcommands and I don't know how to show you the help here")
	
	@audioset.command()
	async def volume(ctx,volume:int):
		self.settings[str(ctx.guild.id)]['volume'] = volume
		self.save_settings()


def check_folders():
	folders = ["data/Audio"]
	for folder in folders:
		if os.path.exists(folder) and os.isdir(folder):
			continue
		else:
			print("Created folder",folder)
			os.makedirs(folder)

def setup(bot):
	check_folders()
	n = Audio(bot)
	bot.add_cog(n)