from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER, nexichat


START_BOT = [
    [
        InlineKeyboardButton(
            text="😍 beni grubuna ekle 😍",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="🥀 sahibi 🥀", user_id=OWNER),
        InlineKeyboardButton(text="✨ ꜱᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(text="« ғᴇᴀᴛᴜʀᴇs »", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(text="🥀 sahibi 🥀", user_id=OWNER),
        InlineKeyboardButton(text="✨ destek ✨", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="✦ beni grubuna ekle ✦",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="« yarım »", callback_data="HELP"),
    ],
    [
        # InlineKeyboardButton(text="❄️ kaynak kod ❄️", callback_data="SOURCE"),
        InlineKeyboardButton(text="☁️ hakkında ☁️", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="😍 beni grubuna ekle 😍",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="⦿ kapat ⦿",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="⦿ geri ⦿", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 chatmode 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 özellikler 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⦿ kapat ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="aktif et", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="kapat", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="son", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⦿ geri ⦿", callback_data="SBACK"),
        InlineKeyboardButton(text="⦿ kapat ⦿", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⦿ geri ⦿", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⦿ kapat ⦿", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="« yarım »", callback_data="HELP"),
        InlineKeyboardButton(text="🐳 kapat 🐳", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="« ʜᴇʟᴘ »", url=f"https://t.me/{nexichat.username}?start=help"
        ),
        InlineKeyboardButton(text="⦿ kapat ⦿", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 destek 🎄", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🍾 sahibi 🍾", user_id=OWNER),
        #   InlineKeyboardButton(text="❄️ kaynak kod ❄️", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="🐳 duyuru 🐳", url=f"https://t.me/{kumsaldestekkanal}"),
        InlineKeyboardButton(text="⦿ geri ⦿", callback_data="BACK"),
    ],
]
