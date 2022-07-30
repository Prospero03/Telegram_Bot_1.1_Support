from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_exit = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [
        InlineKeyboardButton(text='На главную', callback_data='chose_0')
    ]
])
