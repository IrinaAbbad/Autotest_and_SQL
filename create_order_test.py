# Ирина Аббад, поток 08а — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


def test_create_order():
    response = sender_stand_request.post_new_order(data.order_body)
    # В переменную response сохраняется результат запроса на создание заказа
    assert response.status_code == 201


def test_get_order_with_track_number():
    # в переменную track_number сохраняется track номер
    track_number = sender_stand_request.post_new_order(data.order_body).json()['track']
    # В переменную response сохраняется ответ на запрос поиска заказа по track номеру
    response = sender_stand_request.get_order_with_track_number(track_number)
    assert response.status_code == 200
