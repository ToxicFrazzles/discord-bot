import discord
from discord.ext import commands
import json
import asyncio
import os

class Owner:
	def __init__(self,bot):
		self.bot = bot
		self.settings_file = "data/Owner/settings.json"
		try:
			with open(self.settings_file) as f:
				self.settings = json.load(f)
		except FileNotFoundError:
			self.settings = {}
			with open(self.settings_file,"w") as f:
				json.dump(self.settings,f)
	
	async def __global_check(self,ctx):
		is_owner = await self.bot.is_owner(ctx.author)
		return is_owner
	
	def save_settings(self):
		with open(self.settings_file,"w") as f:
			json.dump(self.settings,f)
	
	@commands.command()
	async def load(self,ctx,extension_name:str):
		"""Loads an extension."""
		try:
			self.bot.load_extension("cogs."+extension_name)
			if "cogs" in self.settings and not extension_name in self.settings['cogs']:
				self.settings['cogs'].append(extension_name)
				self.save_settings()
			elif "cogs" not in self.settings:
				self.settings['cogs'] = [extension_name]
				self.save_settings()
		except (AttributeError, ImportError) as e:
			await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
			return
		await ctx.send("{} loaded.".format(extension_name))
	
	@commands.command()
	async def unload(self,ctx,extension_name:str):
		"""Unloads an extension."""
		if extension_name.lower() == "owner":
			await ctx.send("Unloading the cog that is used for loading cogs and stopping the bot is a stupid idea")
			return
		self.bot.unload_extension("cogs."+extension_name)
		if "cogs" in self.settings and extension_name in self.settings['cogs']:
			self.settings['cogs'].remove(extension_name)
		await ctx.send("{} unloaded.".format(extension_name))
	
	@commands.command()
	async def reload(self,ctx,extension_name:str):
		"""Reloads an extension."""
		self.bot.unload_extension("cogs."+extension_name)
		self.bot.load_extension("cogs."+extension_name)
		await ctx.send("{} reloaded.".format(extension_name))
	
	@commands.command()
	async def shutdown(self,ctx,delay:int=0):
		"""Shuts down the bot"""
		await ctx.send("Shutting down. 😴")
		await self.bot.logout()

def check_folders():
	folders = ["data/Owner"]
	for folder in folders:
		if os.path.exists(folder) and os.path.isdir(folder):
			continue
		else:
			print("Created folder",folder)
			os.makedirs(folder)

def setup(bot):
	check_folders()
	bot.add_cog(Owner(bot))
