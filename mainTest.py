import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_validate_time(self):
        self.assertEqual(validate_time("19:00:00"), "ok")
        self.assertEqual(validate_time("24:24:24"), "Неверный формат часов, попробуйте снова")




if __name__ == '__main__':
    unittest.main()
