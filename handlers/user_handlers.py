from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon import lexicon
from random import choice
from keyboards import keyboards
from utils import utils

# инициализируем роутер модуля
router = Router()


# хендлер, срабатывающий на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    # функция проеряет есть ли юзер в словаре, если нет, добавляет с данными
    # по умолчанию
    utils.chek_user(message.from_user.id)
    await message.answer(
        text=choice(lexicon.LEXICON_RU['/start']),
        reply_markup=keyboards.yn_keyboard
        )


# хендлер, срабатывающий на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text=lexicon.LEXICON_RU['/help'],
        reply_markup=keyboards.yn_keyboard
    )


# хендлер, срабатывающий на кнопку "Да"
@router.message(F.text == 'Да! 👌')
async def process_yes_answer(message: Message):
    await message.answer(
        text=choice(lexicon.LEXICON_RU['yes']),
        reply_markup=keyboards.choise_keyboard,
    )


# хендлер, срабатывающий на кнопку "Нет"
@router.message(F.text == 'Нет ⛔')
async def process_no_answer(message: Message):
    await message.answer(text=lexicon.LEXICON_RU['no'])


# хендлер, срабатывающий на выбор юзера в игре
@router.message(F.text.in_(lexicon.options))
async def process_game_answer(message: Message):
    # генерируем рандомный ответ бота
    bot_go = choice(lexicon.options)
    await message.answer(
        text=utils.generate_answer(
            message.text, bot_go, message.from_user.id
            )
        )


# хендлер, срабатывающий на кнопку "аастанавитесь"
@router.message(F.text == 'Аастанавитесь... ⛔')
async def process_stop_command(message: Message):
    await message.answer(
        text=choice(lexicon.LEXICON_RU['stop_phrases']),
        reply_markup=ReplyKeyboardRemove()
        )


# хендлер, срабатывающий на кнопку "Общий счет" (статистика)
@router.message(F.text == 'Общий счет ✏')
async def process_stat_command(message: Message):
    await message.answer(text=utils.stat_func(message.from_user.id))


# хендлер, срабатывающий на сброс статистики
@router.message(F.text == 'Сбросить счет 🗑')
async def process_reset_stat_command(message: Message):
    # сбрасываем стату и генерируем ответ в функции
    ans_string = utils.reset_stat(message.from_user.id)
    await message.answer(
        text=ans_string,
        reply_markup=keyboards.yn_keyboard
        )
