# Домашнее задание по курсу «Тестирование»

## Описание

В данном репозитории представлено выполнение домашних заданий по курсу «Тестирование». Работа состоит из трех задач, каждая из которых направлена на проверку и тестирование различных аспектов программирования и использования API.

## Содержание

1. [Задача №1: Unit-тесты](#задача-1-unit-тесты)
2. [Задача №2: Автотест API Яндекс.Диск](#задача-2-автотест-api-яндексдиск)
3. [Задача №3: Тестирование авторизации с помощью Selenium](#задача-3-тестирование-авторизации-с-помощью-selenium)

## Задача №1: Unit-тесты

### Описание

Написание тестов на три задания из модуля «Основы языка программирования Python».

### Тестируемые функции

1. **Функция `fio`** из модуля `home_work_task_1_fio.py`
    - Функция принимает список с фамилией, именем и отчеством, и возвращает строку из первых букв каждого элемента списка.
2. **Функция `solve`** из модуля `home_work_task_2_palindrome.py`
    - Функция принимает список фраз и возвращает список палиндромов.
3. **Функция `analyze_courses`** из модуля `home_work_task_3_courses_list.py`
    - Функция принимает данные о курсах, наставниках и их длительности, и возвращает информацию о самых коротких и самых длинных курсах.

### Файлы

- `home_work_task_1_fio.py`
- `home_work_task_2_palindrome.py`
- `home_work_task_3_courses_list.py`
- `test_home_work_task_1.py`
- `test_home_work_task_2.py`
- `test_home_work_task_3.py`

### Пример запуска тестов

```
pytest test_home_work_task_1.py
pytest test_home_work_task_2.py
pytest test_home_work_task_3.py
```

## Задача №2: Автотест API Яндекс.Диск

### Описание

Написание тестов для проверки правильности работы Яндекс.Диск REST API. Проверка создания папки на диске с использованием библиотеки `requests`.

### Файлы

- `test_home_work_task_4_YandexDisk.py`

### Пример запуска тестов

```
pytest test_home_work_task_4_YandexDisk.py
```

### Описание тестов

1. **Тест создания папки**
    - Проверка, что API возвращает правильный код ответа при создании папки.
2. **Тест удаления папки**
    - Проверка, что API возвращает правильный код ответа при удалении папки.

### Подготовка

Перед запуском тестов необходимо создать файл `token.txt` с токеном авторизации для Яндекс.Диска.

## Задача №3: Тестирование авторизации с помощью Selenium

### Описание

Написание unit-теста для авторизации на Яндексе с использованием Selenium по URL: https://passport.yandex.ru/auth/

### Файл

- `test_home_work_task_5_authorisation.py`

### Пример запуска тестов

```
pytest test_home_work_task_5_authorisation.py
```

### Описание теста

1. **Тест авторизации на Яндексе**
    - Тест имитирует ввод логина и пароля на странице авторизации Яндекса. Пауза на 30 секунд необходима для ввода кода подтверждения, который приходит на телефон.

## Установка и настройка

1. Установите зависимости:

```
pip install -r requirements.txt
```

1. Убедитесь, что у вас установлен `ChromeDriver` и браузер Google Chrome.
2. Запустите тесты с помощью `pytest`.

## Заключение

Этот проект демонстрирует использование различных инструментов и методов тестирования, таких как unit-тестирование с помощью `unittest` и `pytest`, взаимодействие с API через библиотеку `requests` и автоматизация браузерного тестирования с помощью `Selenium`.