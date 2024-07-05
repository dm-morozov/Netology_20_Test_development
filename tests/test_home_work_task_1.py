import unittest
from home_work_task_1_fio import fio


class TestTaskOneFIO(unittest.TestCase):
    def test_fio_with_params(self):
        for number, (initials, expected, length) in enumerate(
            [
                (['Иванов', 'Иван', 'Иванович'], 'ИИИ', 3),
                (['Жан', 'Клот', 'Вандамович'], 'ЖКВ', 3),
                (['Павлов', 'Иван', 'Уралович'], 'ПИУ', 3),
                (['Семейный', 'Доминик', 'Торретович'], 'СДТ', 3),
            ]
        ):

            with self.subTest(number):
                self.assertEqual(expected, fio(initials))
                self.assertEqual(length, len(initials))

    # @unitest.expectedFailure
    # def test_length_initials(self):
    #     for number, (initials, expected) in enumerate(
    #         [
    #             (['Иванов', 'Иван', 'Иванович'], 3),
    #             (['Жан', 'Клот', 'Вандамович'], 3),
    #             (['Павлов', 'Иван', 'Уралович'], 3),
    #             (['Семейный', 'Доминик', 'Торретович'], 3),
    #         ]
    #     ):

    #         with self.subTest(number):
    #             self.assertEqual(expected, len(initials))