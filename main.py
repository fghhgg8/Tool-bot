import os
import discord
from discord.ext import commands

# Lấy token từ biến môi trường
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN không được cung cấp trong biến môi trường!")

# Khởi tạo bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công với tên: {bot.user}")

bot.run(TOKEN)
