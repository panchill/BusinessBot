    # elif text == '🔶 Финансовый план':
    #     await choose_points_2(message)
    # elif text == '🔶 План производства':
    #     await choose_points_2(message)
    # elif text == '🔶 Оценка рисков':
    #     await choose_points_2(message)
    # elif text == '☑️ Закончить выбор':
    #     await cancel_choose(message)
    # elif text == '🔶 Описание продукции':
    #     await choose_points_2(message)
    # elif text == '🔶 Pest анализ':
    #     await choose_points_2(message)
    # elif text == '🔶 Конкуренты':
    #     await choose_points_2(message)

# bp_points_keyboard = ReplyKeyboardMarkup(
#     keyboard=
# [
#     [
#         KeyboardButton(text='🔶 Анализ рынка'),
#         KeyboardButton(text='🔶 Описание продукции'),
#         KeyboardButton(text='🔶 Маркетинговй план'),
#     ],
#     [
#         KeyboardButton(text='🔶 Финансовый план'),
#         KeyboardButton(text='🔶 План производства'),
#         KeyboardButton(text='🔶 Оценка рисков'),
#     ],
#     {
#         KeyboardButton(text = '🔙 Вернуться назад')
#     }
# ],resize_keyboard=True
# )

# accept_keyboard = ReplyKeyboardMarkup(
#     keyboard=
# [
#     [
#         KeyboardButton(text='✅ Да'),
#         KeyboardButton(text='❌ Нет')
#     ],
#     {
#         KeyboardButton(text = '🔙 Вернуться назад')
#     }
# ],resize_keyboard=True
# )

# questions_keyboard = ReplyKeyboardMarkup(
#     keyboard=
# [
#     [
#         KeyboardButton(text = '☑️ Закончить выбор'),
#         KeyboardButton(text = '📑 Выбрать еще')
#     ],
#     {
#         KeyboardButton(text = '🔙 Вернуться назад')
#     }
# ],resize_keyboard=True
# )


# async def cmd_create_all_plan(message: types.Message):
#     await message.answer("Отлично!\n\nДавайте приступим к заполнению шаблона!", reply_markup=reply.create_plan_keyboard)

# async def choose_points(message: types.Message):
#     await message.answer("Пожалуйста, выберите пункты, которые хотите видеть в своем бизнес-плане:", reply_markup=reply.bp_points_keyboard)  


# async def choose_points_2(message: types.Message):
#     await message.answer("Пункт бизнес-плана добавлен.\nХотите добавить еще?", reply_markup=reply.questions_keyboard)      



# active = False
    # start_found = False
    # delete_after = None

    # # Обработка параграфов
    # for i, para in enumerate(doc.paragraphs):
    #     if start_phrase in para.text:
    #         active = True
    #         start_found = True
    #         continue
    #     elif end_phrase in para.text and start_found:
    #         active = False
    #         delete_after = i
    #         break
    #     if not active:
    #         para._element.clear_content()

    # # Удаление параграфов после точки delete_after
    # if delete_after is not None and len(doc.paragraphs) > delete_after:
    #     while len(doc.paragraphs) > delete_after:
    #         p = doc.paragraphs[delete_after]
    #         p._element.getparent().remove(p._element)

     # Применение замен в оставшихся параграфах