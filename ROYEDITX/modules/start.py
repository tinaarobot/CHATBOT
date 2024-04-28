
import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from ROYEDITX import BOT_NAME, LOCOPILOT, dev
from ROYEDITX.database.chats import add_served_chat
from ROYEDITX.database.users import add_served_user
from ROYEDITX.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    REPO,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@dev.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("❤️")
        await asyncio.sleep(0.2)
        await accha.edit("💚")
        await asyncio.sleep(0.2)
        await accha.edit("💙")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**๏ ʜᴇʏ ʙᴀʙʏ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ... !**\n\n๏ **ɪ ᴀᴍ {BOT_NAME} , ᴀɪ ʙᴀsᴇ ᴄʜᴀᴛʙᴏᴛ.**\n\n๏ **ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ғᴏʀ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ.**\n\n๏ **ᴜsᴇ ᴍᴇ /chatbot on/off ᴀɴᴅ ғᴏʀ ᴍᴏʀᴇ /help ...**""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@dev.on_message(filters.command(["help"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def help(client: LOCOPILOT, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**๏ ʜᴇʏ ʙᴀʙʏ...\n\n๏ ᴘʟᴢ ᴜsᴇ ᴍᴇ ɪɴ ᴘᴠᴛ. ғᴏʀ ʜᴇʟᴏ ᴄᴍᴅs..!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@dev.on_message(filters.command("repo") & ~filters.bot)
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(REPO),
        disable_web_page_preview=True,
    )


@dev.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
          
