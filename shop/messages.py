emoji_plus = '➕'
emoji_minus = '➖'

btn_catalog = 'Каталог'
btn_cart = 'Корзина'
btn_help = 'Доставка'
btn_chat = 'Онлайн-чат'
btn_call = 'Позвонить'
btn_send_phone = 'Отправить номер телефона'
btn_back_to_main_menu = 'Вернуться в главное меню'

btn_add_to_cart = 'Добавить в корзину'
btn_back = '... или продолжить покупки?'
btn_edit_cart = 'Редактировать'
btn_checkout = 'Оформить заказ'
btn_checkout_from_cart = 'Добавили? Оформляем заказ?'
btn_delete = 'Удалить'
btn_back_to_cart = 'Сохранить и вернуться в корзину'
btn_do_nothing = 'Оставляем как есть'

msg_start = '''При заказе через бота скидка 15%!!!'''

msg_main_menu = 'Главное меню'

msg_send_phone = 'Отправьте Ваш номер телефона'

msg_edit_cart = 'Выберите товар, который нужно изменить \nили отредактировать'

msg_empty_cart = 'Ваша корзина пуста'

msg_call = 'Чтобы связаться с оператором, позвоните: +7 (499) 703-00-89'

msg_help = '''<b>Минимальная сумма заказа 690 рублей + доставка!</b>
<i>Скидки при заказе на сумму 690 рублей - НЕ УЧИТЫВАЮТСЯ!</i>
 
<b>Стоимость доставки в пределах МКАД - 390 руб</b>
<i>При заказе на сумму от 5000 руб - скидка 10%, на сумму от 10000 - скидка 15%!</i>
 
<b>Стоимость доставки за пределы МКАД - от 590 до 990 руб</b>
<i>Точная стоимость доставки за МКАД обговаривается с оператором!</i>
 
<b>Оплата через СберБанк онлайн (без комиссии)</b>
<i>Вы можете оплатить ваш заказ через СберБанк онлайн курьеру по факту получения заказа!</i> '''

msg_chat_jivo = 'Перейдите в чат с оператором: @alcopresent_bot'

msg_success = 'Мы получили Ваш заказ. Оператор перезвонит Вам в течение трех минут!'


def msg_new_order(user, order, phone):
    text = f'''Заказ {str(order.id)}:

{user.shopping_cart[-1].shopping_cart_content}

Сумма без доставки: {str(user.shopping_cart[-1].full_sum)} руб.

Заказ оформил {user.first_name}, телефон: {phone}'''
    return text
