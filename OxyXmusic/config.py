
import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAGx2bn3TOO4S_ZHLzoCUquwDwfy0pdA9jYUcQItJDX7SMEhz5nfIu-iL-HJGYAFqKWcScY7_-V7sibMUDopvSKlpwK8iqjtwgsLa-EibFhxe8pBUUAPO7lfJA87TQrwhJDsX7uCZM-XfWQBFjDyEcTv_bIIu2aCo3QGwTKQK6zowlLr0cch2FC26GkAUwfJ0tywiF56B13wYuUnuke0bFe7mLZrENY4dCRzXpqWqHt3JeQVJsWN_-13aLql-h4xmuJPJddPGaKw6Vnz49zCaSO7QsYPCux6TOBv5tuEmGHrmya4SdjCEhVBUW-G7f6JakR0Lro8Gr1hdSD3hyhOdkEb6crEAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1728730929:AAENgSjKZv7UJsbvsdgtuTOPNIOeSPljqOE")
BOT_NAME = getenv("BOT_NAME", "Patricia")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "patricia_updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cdaa3de5adab7ac73689f.png")
admins = {}
API_ID = int(getenv("API_ID", "5786603"))
API_HASH = getenv("API_HASH", "a1354f206a4a05109d0fc916c0f150d0")
BOT_USERNAME = getenv("BOT_USERNAME", "PATRICIA_ROBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "PATRICIAXMUSIC")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "patricia_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "PatriciaMusic")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TEAM-PATRICIA/PatriciaMusic2.0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "UGYJIV-OAQRKE-FFURWI-RDOKKN-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570").split()))
