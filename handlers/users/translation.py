from loader import dp
from aiogram import types
from .tarjimon import tarjima
from keyboards.inline.buttons import button, button1, reply_keyboard
from states.Translator import Holat
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands='tarjima', state=None)
async def com_tarjima(message: types.Message):
    await message.answer('Qaysi tilda matn yubormoqchisiz?', reply_markup=button)
    await Holat.input.set()


@dp.callback_query_handler(Text(startswith='lan'), state=Holat.input)
async def second(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    data = call.data
    await state.update_data({'input': data[3:]})
    await call.message.delete()
    await call.message.answer("Qaysi tilga tarjima qilmoqchisiz?", reply_markup=button1)
    await Holat.next()


# @dp.callback_query_handler(Text(equals='cancel'), state=Holat.input)
# async def cancel(call: types.CallbackQuery, state1: FSMContext):
#     await call.message.delete()
#     await call.message.answer('Buyruq bekor qilindi')
#     await call.message.answer('Tarjimondan foydalanish uchun /tarjima buyg\'idan foydalaning')
#     await state1.finish()


@dp.callback_query_handler(Text(startswith='👍'), state=Holat.output)
async def third(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    data = call.data
    await state.update_data({
        'output': data[1:]
    })
    await call.message.delete()
    await call.message.answer('Tarjima uchun matn kiriting')
    await Holat.next()


# @dp.callback_query_handler(Text(startswith='back'), state=Holat.output)
# async def back(call: types.CallbackQuery, state1: FSMContext):
#     await call.answer(cache_time=30)
#     await call.message.delete()
#     await call.message.answer('Qaysi tilda matn yubormoqchisiz?', reply_markup=button)
#     await Holat.input.set()

@dp.message_handler(text='🔙 Orqaga', state=Holat.text)
async def to_buttons(message: types.Message, state: FSMContext):
    await message.delete()
    await message.answer(text='Qaysi tilda matn yubormoqchisiz?', reply_markup=button)
    await Holat.input.set()

@dp.message_handler(content_types='text', state=Holat.text)
async def test(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({
        'text': text
    })
    data = await state.get_data()
    result = tarjima(data['input'], data['output'], data['text'])
    await message.answer(text='<b>Sizning tarjimangiz:</b>\n'
                         f'<i>{result}</i>', parse_mode='HTML',
                         reply_markup=reply_keyboard)

