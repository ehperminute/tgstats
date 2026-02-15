# main.py - The glorious entry point
import asyncio
from bot.handlers import start_bot

if __name__ == "__main__":
    print("🔥 Starting the dumpster fire...")
    asyncio.run(start_bot())
    print("💀 Bot died. Probably your fault.")
