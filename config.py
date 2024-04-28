from os import getenv

from dotenv import load_dotenv

load_dotenv()

####
API_ID = int(getenv("API_ID", "6435225"))

####
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")

####
BOT_TOKEN = getenv("BOT_TOKEN", None)

####
OWNER_ID = int(getenv("OWNER_ID", "6922271843"))

####
MONGO_URL = getenv("MONGO_URL", None)

####
SUPPORT_GRP = getenv("SUPPORT_GRP", "THE_FRIENDZ")

####
UPDATE_CHNL = getenv("UPDATE_CHNL", "ROY_EDITX")

####
OWNER_USERNAME = getenv("OWNER_USERNAME", "AFK_MR_ROY")

