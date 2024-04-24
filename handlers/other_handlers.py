from aiogram import Router
from aiogram.types import Message
from keyboards.keyboards import yn_keyboard


router = Router()


@router.message()
async def process_other_command(message: Message):
    await message.answer(
        text='Не знаю я таких команд. Пользуйся кнопками. Сыграем?',
        reply_markup=yn_keyboard
        )