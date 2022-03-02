import unittest
from main import *


class MyTestCase(unittest.TestCase):
    # тестирование корректности ввода
    def test_validate_time(self):
        self.assertEqual(validate_time("19:00:00"), "ok")
        self.assertEqual(validate_time("24:24:24"), "Неверный формат часов, попробуйте снова")
        self.assertEqual(validate_time("19:65:24"), "Неверный формат минут, попробуйте снова")
        self.assertEqual(validate_time("19:15:78"), "Неверный формат секунд, попробуйте снова")




if __name__ == '__main__':
    unittest.main()
