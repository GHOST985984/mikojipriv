"""
MIT License

Copyright (c) 2022 ABISHNOI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- Abishnoi69 ""

# ==========================================×========×××=××××××××

import json
import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()


def get_user_list(config, key):
    with open("{}/Miko/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # ᴀᴅᴅ ʏᴏᴜʀ ᴠᴇʀs  (ᴍᴀɪɴ ᴠᴇʀs)
    API_ID = int(getenv("API_ID", "20433698"))
    API_HASH = getenv("API_HASH", "2dfd061fd900a52385873e0ccab30032")
    EVENT_LOGS = int(getenv("EVENT_LOGS", "-1002023182491"))
    DATABASE_URL = getenv(
        "DATABASE_URL",
        "postgres://wsnioboi:Fkf1ef7qRJVP1CvP_gKYqhdxk6LXBbQE@balarama.db.elephantsql.com/wsnioboi",
    )  # elephantsql.com
    REDIS_URL = "redis-cli -u redis://default:uAoinUQfH83lGLZvXYk5nMGHGCQnZL2s@redis-12586.c74.us-east-1-4.ec2.redns.redis-cloud.com:12586"  # redis.os
    MONGO_DB_URL = getenv(
        "MONGO_DB_URL",
        "mongodb+srv://orewauzumaki:orewauzumaki@cluster0.bmhengh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
    TOKEN = getenv("TOKEN", "7916656117:AAEtfNXS7b33yMiWNBRpItPzkuBaVrLAeZM")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "its_damiann")
    OWNER_ID = int(getenv("OWNER_ID", "6848223695"))
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "The_City_of_magicians")

    # ɴᴏᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴢᴏɴᴇ, ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴇᴅɪᴛ
    MONGO_DB = "orewauzumaki"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    ARQ_API_URL = "arq.hamker.dev"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    ARQ_API_KEY = "YZXQNZ-TPCRLZ-HKWWKY-SPPYAL-ARQ"
    DONATION_LINK = "t.me/about_tosuu"
    HELP_IMG = "https://telegra.ph/file/3cc3ffc61293d1687b3bb-8dc0c2ec4d77869def.jpg"
    START_IMG = "https://telegra.ph/file/4890436bf12c47f4e6980-35455c4480d88289d5.jpg"
    UPDATES_CHANNEL = "The_Hogwart"
    INFOPIC = False
    GENIUS_API_TOKEN = (
        "gIgMyTXuwJoY9VCPNwKdb_RUOA_9mCMmRlbrrdODmNvcpslww_2RIbbWOB8YdBW9"
    )
    SPAMWATCH_API = "tBIAzON4MiJmj_WwVbcI3HSXv03xoOZLgQqcZXgQD~6mvM_Gl0fresvC~FoROHKP"
    REM_BG_API_KEY = None
    OPENWEATHERMAP_ID = None
    WALL_API = None
    TIME_API_KEY = None
    NO_LOAD = ["rss"]
    TEMP_DOWNLOAD_DIRECTORY = "./"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    LOAD = []  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEL_CMDS = True
    BAN_STICKER = None
    WORKERS = 8
    STRICT_GBAN = True
    WEBHOOK = False
    URL = None
    PORT = []
    ALLOW_EXCL = []
    AI_API_KEY = "SOME1HING_privet_990022"
    ALLOW_CHATS = True
    CERT_PATH = []
    SPAMWATCH_SUPPORT_CHAT = "The_Hogwart"
    BOT_API_URL = "https://api.telegram.org/bot"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DRAGONS = get_user_list("elevated_users.json", "sudos")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEV_USERS = get_user_list("elevated_users.json", "devs")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    REQUESTER = get_user_list("elevated_users.json", "whitelists")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEMONS = get_user_list("elevated_users.json", "supports")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    INSPECTOR = get_user_list("elevated_users.json", "sudos")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    TIGERS = get_user_list("elevated_users.json", "tigers")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    WOLVES = get_user_list("elevated_users.json", "whitelists")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True


# ENJOY
