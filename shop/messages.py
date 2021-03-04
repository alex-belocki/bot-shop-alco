emoji_plus = '➕'
emoji_minus = '➖'

btn_catalog = 'Каталог'
btn_cart = 'Корзина'
btn_help = 'Помощь'
btn_chat = 'Онлайн-чат'
btn_call = 'Позвонить'
btn_send_phone = 'Отправить номер телефона'
btn_back_to_main_menu = 'Вернуться в главное меню'

btn_add_to_cart = 'Добавить в корзину'
btn_back = '<<< Назад'
btn_edit_cart = 'Редактировать'
btn_checkout = 'Оформить заказ'
btn_delete = 'Удалить'
btn_back_to_cart = 'Сохранить и вернуться в корзину'
btn_do_nothing = 'Оставляем как есть'

msg_start = '''При заказе через бота скидка 15%!!!'''

msg_main_menu = 'Главное меню'

msg_send_phone = 'Отправьте Ваш номер телефона'

msg_edit_cart = 'Выберите товар, который нужно изменить \nили отредактировать'

msg_empty_cart = 'Ваша корзина пуста'

msg_call = 'Чтобы связаться с оператором, позвоните: +7 (499) 703-00-89'

msg_help = 'По всем вопросам пишите на @alco_support'

msg_chat_jivo = 'Перейдите в чат с оператором: @some_bot'

msg_success = 'Мы получили Ваш заказ. Оператор перезвонит Вам в течение трех минут!'


def msg_new_order(user, order):
    text = f'''Новый заказ # {str(order.id)}:

{user.shopping_cart[-1].shopping_cart_content}

Сумма без доставки: {str(user.shopping_cart[-1].full_sum)} руб.

Заказ оформил {user.first_name}, телефон: {user.phone}'''
    return text