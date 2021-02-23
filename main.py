main.py
import discord
from discord.ext import commands

client=commands.bot(command_prefix = '.')

 @client.event
 async def on_ready(): 
      print("the bot is now ready for use!")
    print("--------------------------------")

    @client.command()
    async def hello(ctx):
    await ctx.send("hello, I am the discord bot")

client.run('ODEzNjUyNjY5NzQyMzE3NjM4.YDSbGQ.PIPExsMq70TkfSpjhkOkEn1WhHc')


