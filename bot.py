from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import os

# توکن از Environment Variables گرفته میشه
TOKEN = os.getenv("TELEGRAM_TOKEN")

members = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! برای شرکت در قرعه‌کشی دستور /join را بزنید 🎉")

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    username = user.username or str(user.id)
    if username not in members:
        members.append(username)
        await update.message.reply_text(f"@{username} در قرعه‌کشی ثبت شد ✅")
    else:
        await update.message.reply_text("قبلاً ثبت‌نام کرده‌ای 🙂")

async def draw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if members:
        winner = random.choice(members)
        await update.message.reply_text(f"🎊 برنده: @{winner}")
    else:
        await update.message.reply_text("❌ هنوز کسی ثبت‌نام نکرده!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("draw", draw))
    app.run_polling()

if __name__ == "__main__":
    main()
