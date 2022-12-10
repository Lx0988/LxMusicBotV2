## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "BQAFzZCnmINaY0hhUI3_kJ5_-FDI_ashJtGZ3NX55-rQu2K6zULnnDNh1FNwBE5PiL5RI1Mhq8y4URjfp-pFqSKQv3qq1MfJhzq2V9Be69AWuLcUctLb-cVwDhmUiNLT0sPMDvWDxTwOt4qdN3Q-4jnRxtyhuJpDtJpR3_okw5Yr45jawG2o36YDww_Xpqz0fgtdTF6tA7MkZ_MA8LbHkNuZtPjaaFNGk9iXM5-_usXipldDPyRmX6b8wvC5C2D34iVxYDw9p4OQAyRqSlXrYmvVMGW-p_GbZC59SI6YiZQKA9u4qortUGPK1gapBSfEgmskRgTvzGvRIbNZLPuCs86YAAAAAUSZaVUA":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5300015911:AAFbXSfRiGrxo0aZOzUjQt5zdKI0-7yEZCE")
BOT_NAME = getenv("BOT_NAME", "FlashV2Robot")

API_ID = int(getenv("API_ID", "16029596"))
API_HASH = getenv("API_HASH", "8c6b3ce7f23e51dfebbdbe98a0ee674d")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Media-search:hellourluploder@cluster0.bwyz8wb.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Lx 0980")
OWNER_USERNAME = getenv("OWNER_USERNAME", "FLx0980")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "FlashV2Robot")
OWNER_ID = getenv("OWNER_ID", "1903280447")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BetterAutoFilterBot_Client")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Hollywood_0980")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DFF_UPDATES")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1903280447").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
