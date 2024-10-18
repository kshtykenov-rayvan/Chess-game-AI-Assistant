import requests

# Отправляем GET-запрос
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверяем статус ответа
if response.status_code == 200:
    # Выводим текст ответа (JSON данные)
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")
