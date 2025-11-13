# @sarkari_student

import asyncio
import importlib
import sys
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import idle
from plugins import LOGGER, bot as app
from plugins.modules import ALL_MODULES
from plugins.modules.vsp import load_batches_on_start  # Import the function


async def _start():
    try:
        await app.start()
    except Exception as ex:
        LOGGER.error(f"Failed to start bot: {ex}")
        quit(1)

    # Load all modules dynamically
    for all_module in ALL_MODULES:
        importlib.import_module("plugins.modules." + all_module)

    LOGGER.info(f"@{app.username} Started successfully ✅")

    # Initialize and schedule batches
    try:
        await load_batches_on_start()
        LOGGER.info("Batches loaded and scheduled successfully.")
    except Exception as e:
        LOGGER.error(f"Error during batch loading: {e}")

    # Notify the owner that the bot is online
    try:
        await app.send_message(
            7290128282,
            "**🟢 नमस्ते मालिक! मैं फिर से सक्रिय हो चुका हूँ 🙏🟠**"
        )
    except Exception as e:
        LOGGER.warning(f"Couldn't send start message: {e}")

    # Keep bot running until stopped
    await idle()

    # When stopped (Ctrl+C or restart)
    await app.stop()
    LOGGER.info("Bot stopped cleanly ❌")


if __name__ == "__main__":
    # Fix Windows event loop issues
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        asyncio.run(_start())
    except KeyboardInterrupt:
        LOGGER.info("Bot stopped by user (KeyboardInterrupt).")
    except Exception as e:
        LOGGER.error(f"Unhandled exception: {e}")
