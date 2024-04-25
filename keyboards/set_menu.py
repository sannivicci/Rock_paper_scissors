from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon import menu_commands_ru

async def set_main_menu(bot: Bot):
    menu_commands = [
        BotCommand(
            command=command,
            description=description
            ) for command, description in menu_commands_ru.items()
    ]
    await bot.set_my_commands(menu_commands)