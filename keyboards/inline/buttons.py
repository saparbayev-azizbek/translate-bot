from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data='lanuz'),
            InlineKeyboardButton(text='🇬🇧 Ingliz tili', callback_data='lanen')
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data='lanru'),
            InlineKeyboardButton(text='🇩🇪 Nemis tili', callback_data='lande')
        ],
        [
            InlineKeyboardButton(text="🇦🇪 Arab tili", callback_data='lanar'),
            InlineKeyboardButton(text='🇨🇳 Xitoy tili', callback_data='lanzh-TW')
        ]
        # [
        #     InlineKeyboardButton(text='❌ Bekor qilish', callback_data='cancel')
        # ]
    ]
)
button1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek tili", callback_data='👍uz'),
            InlineKeyboardButton(text='🇬🇧 Ingliz tili', callback_data='👍en')
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Rus tili", callback_data='👍ru'),
            InlineKeyboardButton(text='🇩🇪 Nemis tili', callback_data='👍de')
        ],
        [
            InlineKeyboardButton(text="🇦🇪 Arab tili", callback_data='👍ar'),
            InlineKeyboardButton(text='🇨🇳 Xitoy tili', callback_data='👍zh-TW')
        ]
        # [
        #     InlineKeyboardButton(text='🔙 Orqaga', callback_data='back')
        # ]
    ]
)
reply_keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
reply_keyboard.add(
    KeyboardButton(text='🔙 Orqaga')
)
