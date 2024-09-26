
from aiogram import types, Router, F
from dotenv import find_dotenv, load_dotenv

user_private_router = Router()
load_dotenv(find_dotenv())

from functions import user_inputs
from functions import del_mess
from functions import cmd_return_back
from functions import cmd_create_plan
from functions import cmd_pattern
from functions import cmd_manual
from functions import сmd_about_bot
from functions import cmd_calculate
from functions import cmd_helpful
from functions import cmd_links
from functions import excel_upload
from functions import cmd_benchmarking
from functions import cmd_pest
from functions import cmd_competitors
from functions import cmd_product_description
from API_dwnld_file import get_download_url
from calculating_functions import buttom_back
from calculating_functions import input_clients
from calculating_functions import main_menu_back
from calculating_functions import input_product_cost
from calculating_functions import input_product_cost_TAM
from calculating_functions import input_income
from calculating_functions import input_advert_cost
from calculating_functions import input_quantity_clients
from edit_docx_functions import input_awaiting_company_name


@user_private_router.message(F.text == '🔙 Вернуться назад')        
async def back_router(message: types.Message):
    await cmd_return_back(message)

@user_private_router.message(F.text == '↩️ Вернуться назад')        
async def back_router(message: types.Message):
    await buttom_back(message)

@user_private_router.message(F.text == '🔙 Вернуться в главное меню')        
async def main_menu_back_router(message: types.Message):
    await main_menu_back(message)

@user_private_router.message(F.text == '✍️ Заполнить флаер')        
async def functional_cmd(message: types.Message):
    await cmd_create_plan(message)
    # await message.answer('Эта функция в разработке 😉')

@user_private_router.message()        
async def functional_cmd(message: types.Message):
    text = message.text
    await del_mess(message)
    if text == '✏️ Приступить к заполнению':
        await input_awaiting_company_name(message, user_inputs)
    elif text == '💬 О боте':
        await сmd_about_bot(message)
    elif text == '➕ Вычислить':
        await cmd_calculate(message) 
    elif text == '📝 Полезные материалы':
        await cmd_helpful(message)    
    elif text == '📊 Excel таблицы':
        await excel_upload(message)    
    elif text == '🔗 Полезные ссылки':
        await cmd_links(message)
    elif text == '🔹 Окупаемость инвестиций (ROI)':
        await input_income(message, user_inputs)
    elif text == '🔹 Стоимость клика (CPC)':
        await input_clients(message, user_inputs) 
    elif text == '🔹 Потенциально доступный рынок (PAM)':
        await input_quantity_clients(message, user_inputs)  
    elif text == '🔹 Общий объем рынка (TAM)':
        await input_product_cost_TAM(message, user_inputs)
    elif text == '🔹 Доступная емкость товара (SAM)':
        await input_product_cost(message, user_inputs) 
    elif text == '🔹 Индекс потреб. активности (NPS)':
        await input_clients(message, user_inputs) 
    elif text == '📔 Шаблон бизнес-плана':
        await cmd_pattern(message, get_download_url('disk:/Шаблон БП.docx'))
    elif text == '📖 Методичка':
        await cmd_manual(message, get_download_url('disk:/методичка.docx'))
    elif text == '🔶 Конкуренты':
        await cmd_competitors(message, get_download_url('disk:/competitors.xlsx'))
    elif text == '🔶 Описание продукции':
        await cmd_product_description(message, get_download_url('disk:/product_description.xlsx'))
    elif text == '🔶 Pest анализ':
        await cmd_pest(message, get_download_url('disk:/pest-analysis.xlsx'))
    elif text == '🔶 Бенчмаркинг':
        await cmd_benchmarking(message, get_download_url('disk:/Бенчмаркинг.xlsx'))

