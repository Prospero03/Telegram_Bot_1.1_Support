from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton(text='Не подключается канал', callback_data='chose_1')
    ],
    [
        InlineKeyboardButton(text='Не работает бот', callback_data='chose_2')
    ],
    [
        InlineKeyboardButton(text='Как добавить utm-метку ?', callback_data='chose_3')
    ],
    [
        InlineKeyboardButton(text='Где тех.поддержка ?', callback_data='chose_4')
    ],
    [
        InlineKeyboardButton(text='Как стать партнером TSupport_Bot', callback_data='chose_5')
    ]


])
