import data
import requests
import configurations


# Создание нового заказа: функция возвращает track номер нового заказа
def post_new_order(order_body):
    return requests.post(
        configurations.SERVER_URL + configurations.CREATE_ORDER_URL,  # адрес сервера
        json=order_body,  # тело
        headers=data.headers  # заголовок
    )


# Получения заказа по его track номеру
def get_order_with_track_number(track_n):
    return requests.get(
        configurations.SERVER_URL + configurations.GET_ORDER_WITH_TRACK_N,
        params={'t': track_n}  # параметры для получения заказа по его track номеру
    )
