from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = int(getenv("API_ID", "8236321"))
API_HASH = getenv("API_HASH", "974c0347e3de1ba02b540f07fb970e55")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Im_Ur_Love:ImUrLove@cluster0.5qdpi.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1323020756").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1323020756 1979178376 5203520365").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001761546186"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝙃𝙚𝙧𝙤")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Shailendra34/Hero-OP"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL", "HeroOfficialBots"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP", "Yaaro_ki_yaarii"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1", "")) 

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION", "")) 
