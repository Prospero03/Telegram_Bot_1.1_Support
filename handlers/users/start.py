from aiogram import types
from aiogram.types import CallbackQuery

from keybords.inline import ikb_menu
from keybords.inline import ikb_menu_exit
from loader import dp


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(
        f'<b>Приветствие</b> \n \n {message.from_user.first_name}, выберите раздел по которому у вас есть вопросы 👇 \n',
        reply_markup=ikb_menu)


@dp.callback_query_handler(text='chose_1')
async def send_message(call: CallbackQuery):
    await call.message.answer('<b>Не подключается канал</b>    \n \n Если канал не проявляется в списке TSupport, попробуйте :\n'
                              '1.перейти режим инкогнито (Ctrl+Shift+N);\n'
                              '2.использовать другой браузер;\n'
                              '3.почистить куки и перелогиниться в TSupport;'
                              '4.перезайти в ВК;\n'
                              '5.отключить расширения браузера.\n\n'
                              'Подробнее читайте здесь: ⬇️\n'
                              'https://github.com/Prospero03\n',
                      reply_markup = ikb_menu_exit)


@dp.callback_query_handler(text='chose_2')
async def send_message(call: CallbackQuery):
    await call.message.answer('<b>Не работает бот</b>    \n \n'
                              'Для начала убедимся, что все настройки были соблюдены:\n'
                              '1.Бот активирован.\n'
                              '2.Бот указан в настройках минилендинга или автоматизации по ключевому слову.\n'
                              '3.Подписчик нажал кнопку "Старт" или дал разрешение присылать ему сообщения.\n\n'
                              '⚠️Обратите внимание, что бот НЕ запускается автоматически при подписке на канал.\n'
                              'Его обязательно нужно запустить по кнопке с минилендинга или по ключевому слову, написанному в канал.\n\n'
                              'Если вы все проверели, но бот все равно не запускается, пожалуйста, напишите в тех.поддержку.',
                      reply_markup = ikb_menu_exit)


@dp.callback_query_handler(text='chose_3')
async def send_message(call: CallbackQuery):
    await call.message.answer('<b>UTM-метки</b> \n \n'
                              '✅UTM-метки - параметры, которые добавляются в URL-адреса для получения подробной информации о трафике.'
                              'Их применяют для отслеживания эффективности рекламы и воронки\n'
                              '✅UTM можно использовать для аналитики внутри платформы, экспортировать их во внешние системы или фильтровать подписчиков по ним.\n\n'
                              'Как их добавить к ссылке лендинг ВК или минилендинга читайте здесь: ⬇️\n'
                              'https://github.com/Prospero03',
                      reply_markup = ikb_menu_exit)


@dp.callback_query_handler(text='chose_4')
async def send_message(call: CallbackQuery):
    await call.message.answer('<b>Где тех.поддержка</b> \n \n'
                              'Вы можете написать в нашу тех.поддержку, нажав на кнопку ниже в кабинете TSupportBot. \n'
                              'Подробно распишите свою ситуацию: что делали, какой результат ожидали, что получили в итоге.'
                              'Отправьте ссылки на которые говорите. Это ускорит ответ от тех.поддержки.\n'
                              '✅ Также вы можете написать на почту dimarik03.00rb@gmail.com \n'
                              '✅ Или найти ответы на свои вопросы в разделе помощи с подробными инструкциями:⬇️\n'
                              'https://github.com/Prospero03',
                      reply_markup = ikb_menu_exit)


@dp.callback_query_handler(text='chose_5')
async def send_message(call: CallbackQuery):
    await call.message.answer('<b>Как стать партнером</b>\n \n'
                              'Мы запутили партнерскую программу и теперь 25% с каждого платежа ваших клиентов будет возвращаться вам 💵 \n'
                              'Условия партнерства:\n'
                              '-25% от каждого привлеченного клиента пожизненно.\n'
                              '-бесплатный курс по платформе TSupport для онлайн-школ\n'
                              '-минимальная выплата от 3000 руб.\n'
                              '-личный менеджер, который всегда на связи\n\n'
                              'Регистрируйся прямо сейчас ⬇️\n'
                              'https://github.com/Prospero03 \n'
                              'P.S. Только для юридических лиц и ИП(резидентов РФ).',
                      reply_markup = ikb_menu_exit)


@dp.callback_query_handler(text='chose_0')
async def send_message(call: CallbackQuery):
    await call.message.answer(f'<b>Приветствие</b> \n \n {call.from_user.first_name}, выберите раздел по которому у вас есть вопросы 👇 \n',
                      reply_markup = ikb_menu)

#pip install aiogram --user
#pip install python-dotenv --user
