from aiogram import types

from loader import dp

import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')

@dp.message_handler()
async def sendWiki(message: types.Message):
    print(message.chat.id)
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")
