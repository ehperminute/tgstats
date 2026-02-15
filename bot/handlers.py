# bot/handlers.py - Where commands go to get processed
from telegram.ext import Application, CommandHandler

async def start_command(update, context):
    """When user sends /start"""
    await update.message.reply_text("I'm alive! Send /help")

async def help_command(update, context):
    """When user sends /help"""
    await update.message.reply_text("I don't help. I judge.")

async def start_bot():
    """Start this mess"""
    from config import BOT_TOKEN
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers (more to come)
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    
    print("🤖 Bot is polling... (press Ctrl+C to stop)")
    await app.run_polling()
