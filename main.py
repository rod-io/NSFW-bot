import discord
from discord.ext import commands
from datetime import datetime
import random

client = commands.Bot(command_prefix=".",intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.streaming, name=f".porn"))

@client.command()
async def porn(ctx):    
  if ctx.channel.is_nsfw():
        randomgifs = [
"https://cdn.sex.com/images/pinporn/2022/02/03/26661377.gif?width=460",
"https://cdn.sex.com/images/pinporn/2022/01/28/26631957.gif?width=460",
"https://cdn.sex.com/images/pinporn/2022/01/29/26634321.gif?width=460"]
        await ctx.message.delete()
        embed = discord.Embed(title="",
        color = discord.Colour.random())
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_footer(text="Your Server Name Here")
        embed.timestamp = datetime.utcnow()
        randomgif = random.choice(randomgifs)
        embed.set_image(url=randomgif)
        await ctx.send(embed=embed)
  else:
        embed = discord.Embed(title="`This is not allowed in a SFW channel!`",
        color = discord.Colour.random())
        await ctx.message.delete()
        await  ctx.send(embed=embed, delete_after=2) 

@client.command()
@commands.has_permissions(manage_messages=True)   
async def purge(ctx):
        deleted_messages = await ctx.channel.purge()
        embed = discord.Embed(title=f"`{len(deleted_messages)} pieces of evidence deleted.`",
        color = discord.Colour.random())      
        await  ctx.send(embed=embed, delete_after=2)
 
client.run("Bot Token Here")
