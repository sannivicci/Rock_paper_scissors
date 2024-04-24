from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon import options

# options = ['ножницы ✂', 'бумага 📃', 'камень 🪨']

kb_builder = ReplyKeyboardBuilder()
buttons = [KeyboardButton(text=i) for i in options]
buttons.extend(
    [
        KeyboardButton(text='Аастанавитесь... ⛔'),
        KeyboardButton(text='Общий счет ✏'),
        KeyboardButton(text='Сбросить счет 🗑')
    ]
)
kb_builder.add(*buttons)
kb_builder.adjust(3, 1, 2)

choise_keyboard = kb_builder.as_markup(resize_keyboard=True)

yn_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Да! 👌'), KeyboardButton(text='Нет ⛔')]],
    resize_keyboard=True,
    input_field_placeholder='Жми на кнопки! Не пиши мне!')
