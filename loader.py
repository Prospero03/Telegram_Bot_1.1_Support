from aiogram import Dispatcher, Bot, types

from data import config

bot=Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp=Dispatcher(bot)