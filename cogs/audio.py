import discord
from discord.ext import commands
import asyncio
import os
from time import sleep

class Audio:
	"""Some audio commands"""
	def __init__(bot):
		self.bot=bot
		
	@commands.command
	async def audioset(ctx):
		pass


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
	n = Audio(bot)
	bot.add_cog(n)