import unittest
from datetime import datetime
import sys
import os

# Добавляем путь к модулю class_work_test_0
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from class_work_test_0 import summarize, get_info, multiply
from PhoneBook import PhoneBook


server = 'PROD'

class TestMain(unittest.TestCase):

    @unittest.skipIf(server == 'PROD', "Не реализован")
    def test_summarize1(self):
        a = 5
        b = 7
        expeсted = 12

        result = summarize(a, b)

        self.assertEqual(expeсted, result)

    @unittest.expectedFailure
    def test_summarize2(self):
        a = -5
        b = 8
        expeсted = 3

        result = summarize(a, b)

        self.assertEqual(expeсted, result)

    def test_get_info(self):
        expected = {
            'first_name': 'Timur',
            'last_name': 'Anvartdinov',
            'age': 37,
            'max_age': 40,
        }

        result = get_info()

        self.assertDictEqual(expected, result)

    def test_summarize_with_params(self):
        for number, (a, b, expected) in enumerate([
            (5, 7, 12),
            (-5, 8, 3),
            (5, -7, -2),

        ]):
            with self.subTest(number):
                result = summarize(a, b)
                self.assertEqual(expected, result)

    def test_date(self):
        date = '2024-07-04'
        result = datetime.now().strftime("%Y-%m-%d")

        self.assertEqual(date, result)

    def test_regexp_pattern(self):
        date = '2024-07-04'
        pattern = r"\d{4}-\d{2}-\d{2}"

        self.assertRegex(date, pattern)

class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.phone_book = PhoneBook()

    def tearDown(self) -> None:
        self.phone_book

    def test_create_new_phone_book(self):
        self.assertEqual(0, len(self.phone_book.get_all_contacts()))
    
    def test_create_phone_book(self):
        self.phone_book.add_contact('папа', 1234)
        self.phone_book.add_contact('мама', 12345)
        self.phone_book.add_contact('брат', 1234)

        self.assertEqual(2, len(self.phone_book.get_all_contacts()))