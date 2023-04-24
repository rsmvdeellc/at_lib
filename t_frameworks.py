# Можно выделить три основных фреймворка: unittest, PyTest и nose
# Модуль unittest является встроенным инструментом Python
# PyTest и nose устанавливаются дополнительно, они позволяют получить расширенные возможности


# -- Unittest --
# Тест-раннеры сами находят тестовые методы в указанных при запуске файлах,
# но для этого нужно следовать общепринятым правилам.
# Общее правило для всех фреймворков: название тестового метода должно начинаться со слова "test_".
# Дальше может идти любой текст, который является уникальным названием для теста:
# FEX1:
# def test_name_for_your_test():

# Для unittest существуют собственные дополнительные правила:
# A. Тесты обязательно должны находиться в специальном тестовом классе.
# B. Вместо assert должны использоваться специальные assertion методы.
# FEX2:
# import unittest
#
#
# class TestAbs(unittest.TestCase):
#    def test_abs1(self):
#        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#    def test_abs2(self):
#        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#    unittest.main()


