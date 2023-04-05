import random
import asyncio
import discord
from discord.ext import commands

class LevelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.levels = {}
        self.cooldowns = {}

    @commands.command()
    async def level(self, ctx):
        user_id = ctx.author.id
        if user_id in self.levels:
            level, xp = self.levels[user_id]
            await ctx.send(f"You are currently level {level} with {xp} XP.")
        else:
            await ctx.send("You have not yet gained any XP.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        user_id = message.author.id
        if user_id in self.cooldowns:
            time_since_cooldown = asyncio.get_event_loop().time() - self.cooldowns[user_id][1]
            if time_since_cooldown < self.cooldowns[user_id][0]:
                return
        if user_id in self.levels:
            self.levels[user_id][1] += 5
        else:
            self.levels[user_id] = [1, 5]
        
        self.cooldowns[user_id] = [random.randint(3, 5), asyncio.get_event_loop().time()]
        
    def check_level_up(self):
        for user_id, (level, xp) in self.levels.items():
            if xp >= 100:
                self.levels[user_id][0] += 1
                self.levels[user_id][1] = 0

def setup(bot):
    bot.add_cog(LevelSystem(bot))
