import os
import reply

from aiogram import  Bot, types, F
from aiogram.enums import ParseMode
from edit_docx_functions import send_file
from reply import inline_kb



# Допустимые команды и фразы
acceptable_words = {'📝 Полезные материалы', '✍️ Заполнить флаер', '➕ Вычислить', '💬 О боте', '✔️ Получить файл', '📖 Методичка', '📊 Excel таблицы', '☑️ Закончить выбор', '📑 Выбрать еще', '✅ Да', '❌ Нет', '🔶 Анализ рынка', '🔶 Описание продукции', '🔶 Маркетинговй план', '🔶 Финансовый план', '🔶 План производства', '🔶 Оценка рисков', '↩️ Вернуться назад', '🔙 Вернуться назад', '🔙 Вернуться в главное меню', '📔 Шаблон бизнес-плана', '🔗 Полезные ссылки', '✏️ Приступить к заполнению', '🔹 Окупаемость инвестиций (ROI)', '🔹 Стоимость клика (CPC)', '🔹 Потенциально доступный рынок (PAM)', '🔹 Общий объем рынка (TAM)', '🔹 Доступная емкость товара (SAM)','🔹 Индекс потреб. активности (NPS)', '🔶 Бенчмаркинг', '🔶 Pest анализ', '🔶 Описание продукции', '🔶 Конкуренты'}
del_count = 0
deleted_messages_ids = []
user_inputs = {}

bot = Bot(token=os.getenv('TOKEN'))


async def del_mess(message: types.Message):
    global del_count
    chat_id = message.chat.id
    text = message.text

    # Если сообщение не является допустимой командой или фразой
    if text not in {word for word in acceptable_words}:
        warning_message = await message.answer(f"{message.from_user.first_name}, я понимаю только команды 😥")
        await message.delete()
        del_count += 1
        deleted_messages_ids.append(warning_message.message_id)
        if del_count > 3:
            message_id_to_delete = deleted_messages_ids.pop(0)
            await message.bot.delete_message(chat_id=chat_id, message_id=message_id_to_delete)

async def cmd_calculate(message: types.Message):
    await message.answer("Выберите показатель, который хотите рассчитать:", reply_markup=reply.calculate_keyboard)

async def сmd_about_bot(message: types.Message):
    response = ("<b>Вот, что я могу:</b>\n\n"
                "✅ Помочь создать ваш собственный бизнес-план\n"
                "✅ Произвести финансовый анализ\n"
                "✅ Предоставить обучающие материалы")
    await message.answer(response, parse_mode=ParseMode.HTML, reply_markup=reply.back_keyboard)

async def cmd_return_back(message: types.Message):
    await message.answer('Выберите интересующее действие:', reply_markup=reply.start_keyboard)
    

async def cmd_create_plan(message: types.Message):
    await message.answer("Давайте заполним ваш титульный лист!", reply_markup=reply.create_plan_keyboard)

async def cmd_pattern(message: types.Message, download_url: str):
    await send_file(message.chat.id, download_url, filename="business-plan_sample.docx")
    await message.answer("⏫ Пустой шаблон бизнес-плана ⏫", reply_markup=reply.helpful_keyboard)

async def cmd_manual(message: types.Message, download_url: str):
    await send_file(message.chat.id, download_url, filename="business-plan_manual.docx")
    await message.answer("⏫ Методичка по созданию бизнес плана ⏫", reply_markup=reply.helpful_keyboard)

async def cmd_benchmarking(message: types.Message, download_url: str):
    await send_file(message.chat.id, download_url, filename="benchmarking.xlsx")
    await message.answer("⏫ Бенчмаркинг ⏫", reply_markup=reply.excel_docs_keyboard)

async def cmd_pest(message: types.Message, download_url: str):
    await send_file(message.chat.id, download_url, filename="pest-analysis.xlsx")
    await message.answer("⏫ PEST анализ ⏫", reply_markup=reply.excel_docs_keyboard)

async def cmd_competitors(message: types.Message, download_url: str):
    await send_file(message.chat.id, download_url, filename="competitors.xlsx")
    await message.answer("⏫ Конкуренты ⏫", reply_markup=reply.excel_docs_keyboard)

async def cmd_product_description(message: types.Message, download_url: str):
    await send_file(message.chat.id, download_url, filename="product_description.xlsx")
    await message.answer("⏫ Описание продукции ⏫", reply_markup=reply.excel_docs_keyboard)

async def cancel_choose(message: types.Message):
    await message.answer("Отлично!\n\nДавайте приступим к заполнению шаблона!", reply_markup=reply.create_plan_keyboard)

async def cmd_helpful(message: types.Message):
    await message.answer("Вот, что я могу предоставить:", reply_markup=reply.helpful_keyboard)

async def cmd_links(message: types.Message):
    await message.answer("Вот, что я могу предоставить:", reply_markup=inline_kb)

async def excel_upload(message: types.Message):
    await message.answer("Вот, что я могу предоставить:", reply_markup=reply.excel_docs_keyboard)










       
