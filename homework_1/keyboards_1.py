from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from_time = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

nearest = KeyboardButton(text='Ближайшее')
later = KeyboardButton(text='Позже')

from_time.insert(nearest)
from_time.insert(later)

address = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

fits = KeyboardButton(text='Подходит')
express = KeyboardButton(text='Срочная')
for_time = KeyboardButton(text='Ко времени')

address.insert(fits)
address.insert(express)
address.insert(for_time)