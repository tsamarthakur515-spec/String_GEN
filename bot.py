import os
import asyncio
from pyrogram import Client
from pyrogram.enums import ParseMode
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# ====================== LOAD ENV ======================
load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH, no_updates=True)

# ====================== LOGGER ======================
from logger import after_session_generation

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = """
🟢 **Welcome to James String Generator!**

Professional Session Generator Bot made with ❤️ by Grok.

**How to use:**
1. Send your Telegram phone number (with country code)
2. Receive 5-digit code and send it
3. Get your session string instantly!

**Features:**
• Beautiful UI
• Full session string + .session file
• Works with Pyrogram & Telethon
• 24/7 Online

Made for all beginners & pros!
"""
    await update.message.reply_text(welcome, parse_mode=ParseMode.MARKDOWN)


async def handle_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip()

    if not context.get("phone_sent"):
        if len(text) >= 10 and not text.startswith("+"):
            text = "+" + text.replace(" ", "")
        context["phone_sent"] = True
        context["phone"] = text

        await update.message.reply_text(
            f"✅ **Phone number received:** `{text}`\n\n"
            "Send me the **5-digit code** that Telegram sent you.",
            parse_mode=ParseMode.MARKDOWN
        )
        return

    if not context.get("code_sent"):
        context["code_sent"] = True
        context["code"] = text

        await update.message.reply_text("🔄 **Generating session...** (please wait 5-10 seconds)")

        try:
            # ====================== FIXED LOGIN (VPS ke liye perfect) ======================
            await app.send_code(context["phone"])                    # Code bhejta hai
            await app.sign_in(context["phone"], context["code"])     # Code verify karta hai
            # =============================================================================

            session_string = await app.export_session_string()
            await app.stop()

            file_path = f"{SESSION_NAME}.session"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(session_string)

            reply = f"""✅ **Session Generated Successfully!**

**Session String:**