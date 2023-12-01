from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Qanday yordam kerak?",
            "Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/tarjima - Tarjima")
    
    await message.answer("\n".join(text))
