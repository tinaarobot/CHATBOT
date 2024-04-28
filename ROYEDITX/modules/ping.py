
import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import IMG, OWNER_USERNAME, STICKER
from ROYEDITX import BOT_NAME, dev
from ROYEDITX.database.chats import add_served_chat
from ROYEDITX.database.users import add_served_user
from ROYEDITX.modules.helpers import PNG_BTN


@dev.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="💢",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"**❖ {BOT_NAME} ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ ♥︎\n\n● ᴜᴘᴛɪᴍᴇ ➥ `{ms} ᴍs`**\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ๛ᴀ ᴠ ɪ s ʜ ᴀ ࿐",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
      
