
from aiogram import  types, F
from aiogram.filters import CommandStart
from aiogram.filters import  StateFilter
import reply
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from user_private import user_private_router


class edit_docx(StatesGroup):
    awaiting_company_name = State()
    awaiting_plus1 = State()
    awaiting_plus2 = State()
    awaiting_plus3 = State()
    awaiting_choose1 = State()
    awaiting_choose2 = State()
    awaiting_choose3 = State()
    awaiting_output = State()
    awaiting_number = State()
    awaiting_email = State()
    awaiting_address = State()
    texts = {
    'edit_docx:awaiting_company_name': 'Отлично! Теперь введите название вашей компании.',
    'edit_docx:awaiting_choose1': "Преимущества компании сохранены ✅\n Хотите добавить еще преимущество?",
    'edit_docx:awaiting_choose2': "Преимущества компании сохранены ✅\n Хотите добавить еще преимущество?",
    'edit_docx:awaiting_plus1': "Название компании сохранено✅\nТеперь одним словом или одной фразой опишите преимущества компании:",
    'edit_docx:awaiting_plus2': "Одним словом или одной фразой опишите преимущества компании:",
    'edit_docx:awaiting_plus3': "Одним словом или одной фразой опишите преимущества компании:",
    'edit_docx:awaiting_number': "Преимущества компании сохранены ✅\nТеперь перейдем к заполнению контактов о компании.\nУкажите корпоративный телефон компании:",
    'edit_docx:awaiting_email': "Корпоративный номер сохранен ✅\nУкажите корпоративный email:",
    'edit_docx:awaiting_address': "Корпоративный email сохранен ✅\nУкажите корпоративный адрес:",
    'edit_docx:awaiting_output': 'Корпоративный адрес сохранен ✅',
}

class NPS_coeff(StatesGroup):

    total_users = State()
    promoters = State()
    critics = State()
    texts = {
            'NPS_coeff:total_users' : 'Введите число всех клиентов, которые прошли опрос:',
            'NPS_coeff:promoters' : 'Введите количество клиентов, которые ответили "9-10":',
            'NPS_coeff:critics' : 'Введите количество клиентов, которые ответили "0-6":',
            }
    
@user_private_router.message(StateFilter('*'), CommandStart())
async def main_menu_back(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(f'Привет, {message.from_user.first_name} 👋\nЯ бот-помощник по созданию бизнес плана\n\nЧем я могу вам помочь?', reply_markup=reply.start_keyboard)
    

@user_private_router.message(StateFilter('*'), F.text == '🔙 Вернуться в главное меню')
async def main_menu_back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('Выберите интересующее действие:', reply_markup=reply.start_keyboard)
    await state.clear()

@user_private_router.message(StateFilter('*'), F.text == '↩️ Вернуться назад')
async def buttom_back(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    if current_state == NPS_coeff.total_users:
        await message.answer("Нажмите, чтобы выйти в главное меню", reply_markup=reply.leave_keyboard)
        return
    previous = None

    for step in NPS_coeff.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f'{NPS_coeff.texts[previous.state]}')
            return
        previous = step

    if current_state == SAM_coeff.product_cost:
        await message.answer("Нажмите, чтобы выйти в главное меню", reply_markup=reply.leave_keyboard)
        return
    previous = None

    for step in SAM_coeff.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f'{SAM_coeff.texts[previous.state]}')
            return
        previous = step

    if current_state == TAM_coeff.product_cost:
        await message.answer("Нажмите, чтобы выйти в главное меню", reply_markup=reply.leave_keyboard)
        return
    previous = None

    for step in TAM_coeff.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f'{TAM_coeff.texts[previous.state]}')
            return
        previous = step

    if current_state == ROI_coeff.income:
        await message.answer("Нажмите, чтобы выйти в главное меню", reply_markup=reply.leave_keyboard)
        return
    previous = None

    for step in ROI_coeff.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f'{ROI_coeff.texts[previous.state]}')
            return
        previous = step

    if current_state == CPC_coeff.advert_cost:
        await message.answer("Нажмите, чтобы выйти в главное меню", reply_markup=reply.leave_keyboard)
        return
    previous = None

    for step in CPC_coeff.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f'{CPC_coeff.texts[previous.state]}')
            return
        previous = step

    if current_state == PAM_coeff.quantity_clients:
        await message.answer("Нажмите, чтобы выйти в главное меню", reply_markup=reply.leave_keyboard)
        return
    previous = None

    for step in PAM_coeff.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f'{PAM_coeff.texts[previous.state]}')
            return
        previous = step

    if current_state == edit_docx.awaiting_company_name:
        await message.answer("Нажмите, чтобы выйти в главное меню", reply_markup=reply.leave_keyboard)
        return
    previous = None

    for step in edit_docx.__all_states__:
        if step.state == current_state:
            await state.set_state(previous)
            await message.answer(f'{edit_docx.texts[previous.state]}')
            return
        previous = step
    

@user_private_router.message(StateFilter(None), F.text == '🔹 Индекс потреб. активности (NPS)')
async def input_promotes(message: types.Message, state: FSMContext):
    await message.answer("Введите число всех клиентов, которые прошли опрос:", reply_markup=reply.leave_keyboard)
    await state.set_state(NPS_coeff.total_users)

@user_private_router.message(NPS_coeff.total_users, F.text)
async def input_promotes(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(total_users=message.text)
        await message.answer("Введите количество клиентов, которые ответили '9-10':", reply_markup=reply.back_kb)
        await state.set_state(NPS_coeff.promoters)
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите число всех клиентов, которые прошли опрос:")
    
@user_private_router.message(NPS_coeff.promoters, F.text)
async def input_critics(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(promoters=message.text)
        await message.answer("Введите количество клиентов, которые ответили '0-6':", reply_markup=reply.back_kb)
        await state.set_state(NPS_coeff.critics)
    else:   
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите количество клиентов, которые ответили '9-10':")

@user_private_router.message(NPS_coeff.critics, F.text)
async def input_clients(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(critics=message.text)
        data = await state.get_data()
        total_users = float(data["total_users"])
        promoters = float(data["promoters"])
        critics = float(data["critics"])
        # Расчет ROI (примерная формула)
        NPS = (promoters-critics)/total_users * 100
        # Отправляем результат пользователю
        await message.answer(f"Ваш NPS: {NPS:.2f}%", reply_markup=reply.calculate_keyboard)                                                 
        await state.clear()
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите количество клиентов, которые ответили '0-6':")

class SAM_coeff(StatesGroup):

    product_cost = State()
    quantity_buying_users = State()
    texts = {
            'SAM_coeff:product_cost' : 'Введите цену вашего товара:',
            'SAM_coeff:quantity_buying_users' : 'Введите количество людей покупающих товар и аналоги:',

            }

@user_private_router.message(StateFilter(None), F.text == '🔹 Доступная емкость товара (SAM)')
async def input_product_cost(message: types.Message, state: FSMContext):
    await message.answer("Введите цену вашего товара:", reply_markup=reply.leave_keyboard)
    await state.set_state(SAM_coeff.product_cost)

@user_private_router.message(SAM_coeff.product_cost, F.text)
async def input_quantity_buying_users(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(product_cost=message.text)
        await message.answer("Введите количество людей покупающих товар и аналоги:", reply_markup=reply.back_kb)
        await state.set_state(SAM_coeff.quantity_buying_users)
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите цену вашего товара:")

@user_private_router.message(SAM_coeff.quantity_buying_users, F.text)
async def output(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(quantity_buying_users=message.text)
        data = await state.get_data()
        product_cost = float(data["product_cost"])
        quantity_buying_users = float(data["quantity_buying_users"])
        SAM = product_cost * quantity_buying_users
        # Отправляем результат пользователю
        await message.answer(f"Ваш SAM: {SAM:.2f}", reply_markup=reply.calculate_keyboard)
        await state.clear()
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите количество людей покупающих товар и аналоги:")

class TAM_coeff(StatesGroup):

    product_cost = State()
    quantity_users = State()
    texts = {
            'TAM_coeff:product_cost' : 'Введите цену вашего товара:',
            'TAM_coeff:quantity_users' : 'Введите количество заинтересованных:',

            }

@user_private_router.message(StateFilter(None), F.text == '🔹 Общий объем рынка (TAM)')
async def input_product_cost_TAM(message: types.Message, state: FSMContext):
    await message.answer("Введите цену вашего товара:", reply_markup=reply.leave_keyboard)
    await state.set_state(TAM_coeff.product_cost)

@user_private_router.message(TAM_coeff.product_cost, F.text)
async def input_quantity_users(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(product_cost=message.text)
        await message.answer("Введите количество заинтересованных:", reply_markup=reply.back_kb)
        await state.set_state(TAM_coeff.quantity_users)
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите цену вашего товара:")

@user_private_router.message(TAM_coeff.quantity_users, F.text)
async def output(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(quantity_users=message.text)
        data = await state.get_data()
        product_cost = float(data["product_cost"])
        quantity_users = float(data["quantity_users"])
        TAM = product_cost * quantity_users
        # Отправляем результат пользователю
        await message.answer(f"Ваш TAM: {TAM:.2f}", reply_markup=reply.calculate_keyboard)
        await state.clear()
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите количество заинтересованных:")

class ROI_coeff(StatesGroup):

    income = State()
    expense = State()
    texts = {
            'ROI_coeff:income' : 'Введите ваш доход:',
            'ROI_coeff:expense' : 'Введите ваши расходы:',

            }

@user_private_router.message(StateFilter(None), F.text == '🔹 Окупаемость инвестиций (ROI)')
async def input_income(message: types.Message, state: FSMContext):
    await message.answer("Введите ваш доход:", reply_markup=reply.leave_keyboard)
    await state.set_state(ROI_coeff.income)

@user_private_router.message(ROI_coeff.income, F.text)
async def input_quantity_users(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(income=message.text)
        await message.answer("Введите ваши расходы:", reply_markup=reply.back_kb)
        await state.set_state(ROI_coeff.expense)
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите ваш доход:")

@user_private_router.message(ROI_coeff.expense, F.text)
async def output(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(expense=message.text)
        data = await state.get_data()
        income = float(data["income"])
        expense = float(data["expense"])
        roi = (income - expense) / expense * 100
        # Отправляем результат пользователю
        await message.answer(f"Ваш ROI: {roi:.2f}%", reply_markup=reply.calculate_keyboard)
        await state.clear()
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите количество заинтересованных:")

class CPC_coeff(StatesGroup):

    advert_cost = State()
    quantity_clicks = State()
    texts = {
            'CPC_coeff:advert_cost' : 'Введите стоимость вашей рекламы:',
            'CPC_coeff:quantity_clicks' : 'Введите количество кликов:',

            }

@user_private_router.message(StateFilter(None), F.text == '🔹 Стоимость клика (CPC)')
async def input_advert_cost(message: types.Message, state: FSMContext):
    await message.answer("Введите стоимость вашей рекламы:", reply_markup=reply.leave_keyboard)
    await state.set_state(CPC_coeff.advert_cost)

@user_private_router.message(CPC_coeff.advert_cost, F.text)
async def input_quantity_users(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(advert_cost=message.text)
        await message.answer("Введите количество кликов:", reply_markup=reply.back_kb)
        await state.set_state(CPC_coeff.quantity_clicks)
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите стоимость вашей рекламы:")


@user_private_router.message(CPC_coeff.quantity_clicks, F.text)
async def output(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(quantity_clicks=message.text)
        data = await state.get_data()
        advert_cost = float(data["advert_cost"])
        quantity_clicks = float(data["quantity_clicks"])
        CPC = advert_cost / quantity_clicks
        # Отправляем результат пользователю
        await message.answer(f"Ваш CPC: {CPC:.2f}", reply_markup=reply.calculate_keyboard)
        await state.clear()
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите количество кликов:")

class PAM_coeff(StatesGroup):

    quantity_clients = State()
    cost_of_system = State()
    texts = {
            'PAM_coeff:quantity_clients' : 'Введите количество потенциальных клиентов:',
            'PAM_coeff:cost_of_system' : 'Введите стоимость системы:',

            }

@user_private_router.message(StateFilter(None), F.text == '🔹 Потенциально доступный рынок (PAM)')
async def input_quantity_clients(message: types.Message, state: FSMContext):
    await message.answer("Введите количество потенциальных клиентов:", reply_markup=reply.leave_keyboard)
    await state.set_state(PAM_coeff.quantity_clients)

@user_private_router.message(PAM_coeff.quantity_clients, F.text)
async def input_quantity_users(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(quantity_clients=message.text)
        await message.answer("Введите стоимость системы:", reply_markup=reply.back_kb)
        await state.set_state(PAM_coeff.cost_of_system)
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите количество потенциальных клиентов:")

@user_private_router.message(PAM_coeff.cost_of_system, F.text)
async def output(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(cost_of_system=message.text)
        data = await state.get_data()
        quantity_clients = float(data["quantity_clients"])
        cost_of_system = float(data["cost_of_system"])
        PAM = quantity_clients * cost_of_system
        # Отправляем результат пользователю
        await message.answer(f"Ваш PAM: {PAM:.2f}", reply_markup=reply.calculate_keyboard)
        await state.clear()
    else:
        await message.answer("На этом этапе я понимаю только числа 😰\nВведите стоимость системы:")


