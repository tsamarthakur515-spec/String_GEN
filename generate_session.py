from pyrogram import Client
import os

API_ID = int(input("API ID: ").strip())
API_HASH = input("API HASH: ").strip()

SESSION_NAME = "my_session"

app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

with app:
    print("\nGenerating session...")
    session_string = app.export_session_string()

    print("\n" + "=" * 60)
    print("STRING SESSION")
    print("=" * 60)
    print(session_string)
    print("=" * 60)

    with open("session_string.txt", "w") as f:
        f.write(session_string)

    print("\nSaved locally: session_string.txt")