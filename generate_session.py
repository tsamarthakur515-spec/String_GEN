from pyrogram import Client
from pyrogram.errors import (
    ApiIdInvalid,
    ApiIdPublishedFlood,
    AuthKeyUnregistered,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
)
import sys

SESSION_NAME = "my_session"


def get_input(prompt):
    value = input(prompt).strip()

    if not value:
        print("Input empty hai.")
        sys.exit(1)

    return value


def main():
    print("=" * 60)
    print("       TELEGRAM STRING SESSION GENERATOR")
    print("=" * 60)

    try:
        api_id = int(get_input("API ID: "))
    except ValueError:
        print("API ID number hona chahiye.")
        return

    api_hash = get_input("API HASH: ")

    app = Client(
        SESSION_NAME,
        api_id=api_id,
        api_hash=api_hash,
    )

    try:
        print()
        print("Telegram login start ho raha hai...")
        print()

        with app:
            session_string = app.export_session_string()

        if not session_string:
            print("Session generate nahi hua.")
            return

        with open(
            "session_string.txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(session_string)

        print()
        print("=" * 60)
        print("SESSION GENERATED")
        print("=" * 60)
        print()
        print(session_string)
        print()
        print("=" * 60)
        print("Saved locally: session_string.txt")
        print("=" * 60)

    except ApiIdInvalid:
        print("API ID ya API HASH invalid hai.")

    except ApiIdPublishedFlood:
        print("API ID par Telegram flood restriction hai.")

    except PhoneCodeInvalid:
        print("Login code invalid hai.")

    except PhoneCodeExpired:
        print("Login code expire ho gaya.")

    except SessionPasswordNeeded:
        print("2FA password required hai.")

    except AuthKeyUnregistered:
        print("Telegram authorization key invalid hai.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()