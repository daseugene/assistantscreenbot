from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardMarkup, ReplyKeyboardRemove


main_buttons = InlineKeyboardMarkup(row_width=1).row(
    *(
        InlineKeyboardButton(
            "Получить код",
            callback_data='send_code'
        )
    )
)