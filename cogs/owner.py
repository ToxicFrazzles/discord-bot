import discord
from discord.ext import commands

class Owner:
	def __init__(self,bot):
		self.bot = bot
	
	async def __global_check(self,ctx):
		is_owner = await self.bot.is_owner(ctx.author)
		return is_owner
	
	@commands.command()
	async def load(self,ctx,extension_name:str):
		"""Loads an extension."""
		try:
			self.bot.load_extension(extension_name)
		except (AttributeError, ImportError) as e:
			await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
			return
		await ctx.send("{} loaded.".format(extension_name))
	
	@commands.command()
	async def unload(self,ctx,extension_name:str):
		"""Unloads an extension."""
		self.bot.unload_extension(extension_name)
		await ctx.send("{} unloaded.".format(extension_name))

def setup(bot):
	bot.add_cog(Owner(bot))
