import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot đã đăng nhập: {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Thay YOUR_TOKEN bằng token thật hoặc để trống nếu dùng biến môi trường
bot.run(os.getenv("DISCORD_TOKEN"))
