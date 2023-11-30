import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Subhi",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="Subhi"),
)


if __name__ == "__main__":
    print("ꜱᴛᴀʀᴛɪɴɢ ꜱᴜʙʜɪ ꜱᴛʀɪɴɢ ʙᴏᴛ❤️...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} 【ＳＴＡＲＴＥＤ　ＳＵＣＥＳＳＦＵＬＬＹ】. ♥ MADE BY ♥ ꜱᴜʙʜɪ ʟᴏᴠᴇ 🤗")
    idle()
    app.stop()
    print("𝙱𝙾𝚃 𝚂𝚃𝙾𝙿𝙿𝙴𝙳 𝙱𝚈 !")
