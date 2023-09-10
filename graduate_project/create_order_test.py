# Марина Гарафутдинова, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

#Тест. Создание заказа.

def test_create_new_order():
    order_response = sender_stand_request.post_new_order(data.order_body)
    assert order_response.status_code == 201

