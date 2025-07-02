import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN không được cung cấp trong biến môi trường!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công với tên: {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Xin chào!")

bot.run(TOKEN)
