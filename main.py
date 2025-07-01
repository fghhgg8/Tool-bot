import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Bắt buộc phải bật nếu bạn muốn đọc nội dung tin nhắn

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập thành công với tên: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Lấy token từ biến môi trường
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("❌ DISCORD_TOKEN không được cung cấp trong biến môi trường!")

# Khởi chạy bot
bot.run(TOKEN)
