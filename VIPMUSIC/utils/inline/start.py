from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ ʜᴇʟᴘ ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ ꜱᴇᴛᴛɪɴɢꜱ  ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="✡ ɢʀᴏᴜᴘ ✡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁 α∂∂ мє ιη уσυя gяσυρ 𖠁⃝╾─•",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="•─╼⃝𖠁 ɢʀᴏᴜᴘ ", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="мσяє 𖠁⃝╾─•", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text=" ᴄᴏᴍᴍᴀɴᴅꜱ ", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
