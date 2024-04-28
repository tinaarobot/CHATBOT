from pyrogram import filters
from pyrogram.types import Message

from ROYEDITX import OWNER, dev
from ROYEDITX.database.chats import get_served_chats
from ROYEDITX.database.users import get_served_users


@dev.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: dev, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴀʟʟ sᴛᴀᴛs ᴏғ ɴʏᴋᴀᴀ ᴄʜᴀᴛʙᴏᴛ {(await cli.get_me()).mention} :

๏ **ᴄʜᴀᴛs ➛** {chats}
๏ **ᴜsᴇʀs ➛** {users}"""
    )
  
