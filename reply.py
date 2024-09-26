from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text = '📝 Полезные материалы'),
            KeyboardButton(text = '✍️ Заполнить флаер'),   
        ],
        {
            KeyboardButton(text = '➕ Вычислить'),
            KeyboardButton(text = '💬 О боте'),
            
        }
    ],
   resize_keyboard=True,
   input_field_placeholder='Что вас интересует?'
)

back_kb = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text = '↩️ Вернуться назад'),
        ]
    ],resize_keyboard=True
)

back_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text = '🔙 Вернуться назад'),
        ]
    ],resize_keyboard=True
)

leave_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text = '🔙 Вернуться в главное меню'),
        ]
    ],resize_keyboard=True
)

accept_keyboard = ReplyKeyboardMarkup(
    keyboard=
[
    [
        KeyboardButton(text='✅ Да'),
        KeyboardButton(text='❌ Нет')
    ],
],resize_keyboard=True
)

create_plan_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text = '✏️ Приступить к заполнению'),
            KeyboardButton(text = '🔙 Вернуться назад'),
        ],
    ],resize_keyboard=True
)


upload_file_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text = '✔️ Получить файл'),
        ]
    ],resize_keyboard=True
)


excel_docs_keyboard = ReplyKeyboardMarkup(
    keyboard=
[
    [
        KeyboardButton(text='🔶 Конкуренты'),
        KeyboardButton(text='🔶 Описание продукции'),
        
    ],
    [
        KeyboardButton(text='🔶 Pest анализ'),
        KeyboardButton(text='🔶 Бенчмаркинг'),
    ],
    {
        KeyboardButton(text = '🔙 Вернуться назад')
    }
],resize_keyboard=True


)




calculate_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text = '🔹 Окупаемость инвестиций (ROI)'),
            KeyboardButton(text = '🔹 Стоимость клика (CPC)'),
            KeyboardButton(text = '🔹 Доступная емкость товара (SAM)'),
        ],
        [
            KeyboardButton(text = '🔹 Потенциально доступный рынок (PAM)'),
            KeyboardButton(text = '🔹 Общий объем рынка (TAM)'),
            KeyboardButton(text = '🔹 Индекс потреб. активности (NPS)'),
        ],
        {
            KeyboardButton(text = '🔙 Вернуться назад')
        },
    ],resize_keyboard=True
)

helpful_keyboard = ReplyKeyboardMarkup(
    keyboard=
    [
        [
            KeyboardButton(text = '📔 Шаблон бизнес-плана'),
            KeyboardButton(text = '🔗 Полезные ссылки'),
        ],
        [
            KeyboardButton(text = '📖 Методичка'),
            KeyboardButton(text = '📊 Excel таблицы'),
        ],
        {
            KeyboardButton(text = '🔙 Вернуться назад')
        }      
    ],resize_keyboard=True
)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
    InlineKeyboardButton(text ='💰 Маркетинговый план', url='https://sendpulse.com/ru/support/glossary/marketing-plan'),
        ],
        [
    InlineKeyboardButton(text = '📊 Политика ценообразования', url='https://www.fd.ru/articles/161871-politika-tsenoobrazovaniya'),
        ],
        [
    InlineKeyboardButton(text = '📑 Описание продукта', url='https://www.openbusiness.ru/biz/business/shag-pyatyy-opisanie-produktsii-i-uslug/'),
        ],
        ]
    )