from class_work_test_0 import summarize, get_info, multiply


def tests():
    try:
        assert summarize(-5, 8) == 3, 'Ожидаемое значение: 3'
        assert multiply(2, 3) == 6, 'Ожидаемое значение: 6'
        assert get_info() == {
            'first_name': 'Timur',
            'last_name': 'Anvartdinov',
            'age': 37,
            'max_age': 40,
        }
    except AssertionError as e:
        print(e)
    finally:
        print('Проверка завершена!')


# tests()

def test_summarize(a, b, expected):
    result = summarize(a, b)
    try:
        assert result == expected
        print(f"Тест Пройден. На параметрах {a} и {b}." \
              f" Ожидаемое значение: {expected}, получено: {result}")
    except AssertionError as e:
        print(f"Тест провален. На параметрах {a} и {b}." \
              f" Ожидаемое значение: {expected}, получено: {result}")
    finally:
        print('\nПроверка завершена!')

test_summarize(3, 8, 11)
test_summarize(-5, 8, 3)
test_summarize(-6, -8, -14)
