from fastapi.testclient import TestClient
from app.main import app
from app.models import SessionLocal, Order

client = TestClient(app)


def test_create_order():
    # Отправляем запрос на создание заказа
    response = client.post("/orders/", json={"text_query": "test_image", "user_id": 1})

    # Проверяем, что заказ был успешно создан
    assert response.status_code == 200
    assert response.json() == {"message": "Order received and added to the queue"}

    # Проверяем, что заказ добавлен в базу данных
    session = SessionLocal()
    order = session.query(Order).filter(Order.text_query == "test_image").first()
    assert order is not None
    session.close()

# Добавить тесты:
# - Проверку генерации изображения (это может потребовать мокирование функции генерации изображения)
# - Проверку обработки ошибок (например, неверные параметры запроса)
# - Проверку других маршрутов и функций вашего приложения
