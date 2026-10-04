from pyrogram import Client
from pyrogram.errors import (
    ApiIdInvalid,
    ApiIdPublishedFlood,
    AuthKeyUnregistered,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
)
import os
import sys


SESSION_NAME = "my_session"


def get_input(prompt):
    value = input(prompt).strip()
    if not value:
        print("❌ Input empty hai.")
        sys.exit(1)
    return value


def main():
    print("=" * 60)
    print("        TELEGRAM STRING SESSION GENERATOR")
    print("=" * 60)
    print()
    print("Ye session locally save hoga.")
    print()

    try:
        api_id = int(get_input("API ID: "))
    except ValueError:
        print("❌ API ID number hona chahiye.")
        return

    api_hash = get_input("API HASH: ")

    client = Client(
        SESSION_NAME,
        api_id=api_id,
        api_hash=api_hash,
    )

    try:
        print("\n🔄 Telegram login start ho raha hai...\n")

        with client:
            session_string = client.export_session_string()

        if not session_string:
            print("❌ Session generate nahi hua.")
            return

        with open("session_string.txt", "w", encoding="utf-8") as file:
            file.write(session_string)

        print("=" * 60)
        print("✅ SESSION GENERATED")
        print("=" * 60)
        print()
        print(session_string)
        print()
        print("=" * 60)
        print("✅ Local file: session_string.txt")
        print("=" * 60)

    except ApiIdInvalid:
        print("❌ API ID/API HASH invalid hai.")

    except ApiIdPublishedFlood:
        print("❌ API ID par Telegram flood