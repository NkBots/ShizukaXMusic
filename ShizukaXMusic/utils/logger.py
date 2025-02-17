from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from ShizukaXMusic.utils.database import is_on_off
from ShizukaXMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""


**Name : ›** {message.from_user.mention}

**Username : ›** @{message.from_user.username}

**ID : ›** `{message.from_user.id}`

**Chat link: >** {chatusername}

**Searched For:** {message.text}**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
