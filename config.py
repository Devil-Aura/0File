import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", ":")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22768311"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "702d8884f48b42e865425391432b3794")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002436399053"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Devil")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6040503076"))
#Port
PORT = os.environ.get("PORT", "8530")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://helloworld2025:iamrealspyer01@cluster0.xpucres.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "1800"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002648489600"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002412965164"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/9mJXtDNr/x.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/9mJXtDNr/x.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = False if os.environ.get('TOKEN', "False") == "False" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "0")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "0")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 0)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","0")


HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @CrunchyRollChannel\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ └/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/World_Fastest_Bots>World Fastest Bots™</a></blockquote></b>"

ABOUT_TXT = "<b><blockquote>◈🤖 My Name :<a> href='https://telegra.ph/Crunchy-Roll-Vault-04-08'>Crunchyroll Vault</a>\n◈ Anime Channel : <a href=https://t.me/Crunchyrollchannel>Crunchyroll Channel</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/World_Fastest_Bots>World Fastest Bots</a></blockquote></b>"


START_MSG = os.environ.get("START_MESSAGE","""<b>ʜᴇʏ {first}!</b>\n\n<b>ᴍᴇʀᴀ ɴᴀᴀᴍ <u>Crunchyroll Vault</u> ʜᴀɪ, ᴍᴀɪ ᴇᴋ ʙᴏᴛ ʜᴜ.</b>\n<b><blockquote>ᴍᴀɪ ᴀᴀᴘᴋᴏ ᴀɴɪᴍᴇ ᴇᴘɪꜱᴏᴅᴇꜱ ᴀᴜʀ ᴘᴜʀᴇ ᴀɴɪᴍᴇꜱ ʜɪɴᴅɪ ᴅᴜʙ ᴍᴇɪɴ ᴅᴇᴛᴀ ʜᴜ.</b>\n<b>ᴀɢᴀʀ ᴀᴀᴘᴋᴏ ᴏʀ ᴀɴɪᴍᴇꜱ ᴄᴀʜɪʏᴇ ᴛᴏʜ, ʜᴀᴍᴀʀᴇ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ᴋᴏ ᴊᴏɪɴ ᴋᴀʀᴏ!<blockquote></b>""")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 5231212075 7328629001").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", """<b>ʀᴏᴋᴏ {first}!</b>\n\n<b>ᴛᴜᴍɴᴇ ᴀʙʜɪ ᴛᴀᴋ ʜᴀᴍᴀʀᴀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ ᴊᴏɪɴ ɴᴀʜɪɴ ᴋɪʏᴀ ʜᴀɪ!</b>\n<b><blockquote>ᴀɴɪᴍᴇ ᴋᴇ ᴇᴘɪꜱᴏᴅᴇꜱ ᴀᴜʀ ᴘᴜʀᴇ ᴀɴɪᴍᴇꜱ ʜɪɴᴅɪ ᴍᴇɪɴ ᴅᴇᴋʜɴᴇ ᴋᴇ ʟɪʏᴇ, ᴘᴇʜʟᴇ ʜᴀᴍᴀʀᴇ ᴄʜᴀɴɴᴇʟꜱ ᴊᴏɪɴ ᴋᴀʀɴᴀ ʜᴏɢᴀ।</b>\n<b>ꜱᴀʙ ᴄʜᴀɴɴᴇʟꜱ ᴊᴏɪɴ ᴋᴀʀɴᴇ ᴋᴇ ʙᴀᴀᴅ /start ʟɪᴋʜᴏ ᴀᴜʀ ᴍᴀᴢᴀ ʟᴜᴛᴏ!<blockquote></b>""")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Crunchyrollchannel</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!! ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - @CrunchyRollChannel.</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
