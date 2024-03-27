# Тестовый проект с использованием Selenium в Python

Этот проект представляет собой пример использования библиотеки Selenium для автоматизации веб-тестирования

## Функциональность

1. Открытие сайта Rambler.ru
2. Логин в почту на Rambler.ru
3. Проверка успешного входа
4. Поиск писем во входящих с определённой темой
5. Отправка сообщения на почту с количеством найденных писем

## Используемые инструменты

- Python
- Selenium WebDriver
- Pytest
- Allure

## Инструкции по установке и запуску

1. Откройте среду разработки для Python
2. Установите библиотеки, перечисленные в файле `requirements.txt`, с помощью команды: pip install -r requirements.txt
3. Установите Allure
4. Запустите тесты с помощью Pytest и генерируйте отчеты Allure:
pytest --alluredir=allure-results
allure serve allure-results


## Примечания

- Для успешного выполнения тестов вам потребуется аккаунт на сайте Rambler.ru
- Перед запуском тестов убедитесь, что ваши учетные данные для входа в почту указаны в файле `config.py`.

