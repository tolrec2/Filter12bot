from pyrogram import Client, filters 
from info import JOIN_CHANNELS
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from datetime import datetime, timedelta

@Client.on_message(filters.command("joinchannels") & filters.incoming & filters.private)
async def check_joined(client, message):
    sts = await message.reply("Checking......")
    text = "<b><---×××Check Our Channel List×××---></b>\n\n"
    buttons = []
    for i, channel in enumerate(JOIN_CHANNELS, start=1):
        chat = await client.get_chat(channel)
        text += f"<b>{i}:- {chat.title}: </b>"
        try:
            await client.get_chat_member(chat_id=channel, user_id=message.from_user.id)
        except UserNotParticipant:
            now = datetime.now()
            revoke_time = now + timedelta(minutes=3)
            text += "❌"
            invite_link = (await client.create_chat_invite_link(chat_id=channel, expire_date=revoke_time, creates_join_request=False)).invite_link
            buttons.append([InlineKeyboardButton(chat.title, url=invite_link)])
        else:
            text += "✅"
        text += "\n"
    await sts.edit(text=text, reply_markup=InlineKeyboardMarkup(buttons) if buttons != [] else None)
 
