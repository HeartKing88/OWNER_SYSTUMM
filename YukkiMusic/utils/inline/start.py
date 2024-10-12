#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#
from pyrogram.types import InlineKeyboardButton

import config
from YukkiMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_9"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_8"], callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_3"], url=config.SUPPORT_CHAT),
            
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_6"], callback_data="gib_source"),
        ],
    ]


    def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✿︎ ᴀᴅᴅ ᴍᴇ ✿︎", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons
