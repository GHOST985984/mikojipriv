from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from Miko import DEV_USERS
from Miko import pgram as pbot


def can_restrict(func: Callable) -> Callable:
    def non_admin(_, message: Message):
        if message.from_user.id in DEV_USERS:
            return func(_, message)

        check = pbot.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return message.reply_text(
                "» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴘʟᴇᴀsᴇ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs."
            )

        admin = pbot.get_chat_member(message.chat.id, message.from_user.id).privileges
        if admin.can_restrict_members:
            return func(_, message)
        else:
            return message.reply_text(
                "`You don't have permissions to restrict users in this chat."
            )

    return non_admin
