import aiohttp
import asyncio
import mimetypes
import json
import discord
from discord.ext import commands

class NSFW(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'gay', pass_context=True, help = 'Get a gay yiff image')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def gay(self, ctx):
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/nsfw/yiff/gay/") as resp:
                data = await resp.text()
                data = json.loads(data)
        embed = discord.Embed(title = "Oh murr!", description = "I hope you enjoy this image ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'blowjob', pass_context=True, help = 'Get a gay blowjob image')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def blowjob(self, ctx):
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/nsfw/yiff/blowjob/") as resp:
                data = await resp.text()
                data = json.loads(data)
        embed = discord.Embed(title = "Oh murr!", description = "I hope you enjoy this image ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'yiff', pass_context=True, help = 'Yiff someone else')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def yiff(self, ctx, *, users):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
            
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/nsfw/yiff/gay/") as resp:
                data = await resp.text()
                data = json.loads(data)
        
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Hope you like it rough!", description = f"{self.bot.user.mention} pulls {users} on the bed, whips out their massive hybrid cock, and starts to yiff them like there's no tomorrow. \n\nGood luck walking tomorrow ;)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you wanna fuck me?", description = f"I'm surprised, {ctx.message.author.mention}.. Is a bot really worth fucking? \n\nOkay then, top or bottom? ;)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Hope you like it rough!", description = f"{ctx.message.author.mention} pulls {users} on the bed and starts to yiff them like there's no tomorrow. \n\nGood luck walking tomorrow, guys ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'suck', pass_context=True, help = 'Suck off someone else')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def suck(self, ctx, *, users):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
            
        data = ""
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/nsfw/yiff/blowjob/") as resp:
                data = await resp.text()
                data = json.loads(data)
        
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Down the hatch!", description = f"{self.bot.user.mention} lays on the bed, whilst {ctx.message.author.mention} sucks them off. Such a good slut ;)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you wanna fuck me?", description = f"I'm surprised, {ctx.message.author.mention}.. Is a bot really worth sucking off? \n\nOkay then, I'm game ;)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Hope you like it rough!", description = f"{users} lays on the bed, whilst {ctx.message.author.mention} sucks them off. Such a good slut ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0')
        return await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(NSFW(bot))