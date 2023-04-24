# -- Сообщения об ошибках --

# Если значение выражения истинно - сообщений не будет:
# assert abs(-42) == 42

# Если условие не выполнено, то в консоли выводится лог ошибки с названием файла и номером строчки,
# в которой произошла ошибка, а также тип ошибки AssertionError

# Добавление информативности к сообщению AssertionError после зпт
# assert abs(-42) == -42, "Should be absolute value of a number"


# -- Составные сообщения об ошибках --

# 1. Проверка наличия элемента:
# assert self.is_element_present('create_class_button', timeout=30), "No create class button"

# 1.1 Если элемент встречается на нескольких страницах:
# assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"

# 2. Форматирование строк с помощью конкатенации:
# actual_result = "texttexttext"
# print("Wrong text, got " + actual_result + ", something wrong")

# 3. Форматирование строк с помощью str.format:
# "Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")
# print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
# Результат выполнения:
# Let's count together: one, then goes two, and then three

# 4. Форматирование строк с помощью f-strings:
# - Fex1:
# str1 = "one"
# str2 = "two"
# str3 = "three"
# print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")
# Результат выполнения:
# Let's count together: one, then goes two, and then three
# - Fex2:
# actual_result = "texttexttext"
# f"Wrong text, got {actual_result}, something wrong"
# Результат выполнения:
# Wrong text, got texttexttext, something wrong
# - Fex3:
# f"{2+3}"

# 5. Поиск подстроки
# Иногда при работе с текстами не нужны жёсткие проверки на полное совпадение
# и требуется проверить, что некий текст является подстрокой другого текста.
# Это можно сделать либо с помощью ключевого слова in, либо с помощью функции find:
# a)
# s = 'My Name is Julia'
# if 'Name' in s:
#     print('Substring found')
# b)
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')
#
# Конструкция 'Name' in s возвращает просто True или False,
# a find() возвращает индекс первого вхождения подстроки в строку и -1,
# если подстрока не найдена. Обычно в автотестах достаточно использовать in,
# потому что это более читабельный вариант.
# Например, для проверки того, что в текущем url содержится строка login:
# assert "login" in browser.current_url, # сообщение об ошибке


# -- Задача на составные сообщения об ошибках --
# Вам дана функция test_input_text,  которая принимает два значения:
# expected_result — ожидаемый результат, и actual_result — фактический результат.
# Обратите внимание, input использовать не нужно!
# Функция должна проверить совпадение значений с помощью оператора assert
# и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.
# Важно! Формат ошибки должен точно совпадать с приведенным в примере,
# чтобы его засчитала проверяющая система.
# Тестируется через stdin → stdout
# Sample Input 1: 8 11
# Sample Output 1: expected 8, got 11
# Sample Input 2: 11 11
# Sample Output 2:
# Sample Input 3: 11 15
# Sample Output 3: expected 11, got 15
#
# def test_input_text(expected_result, actual_result):
#    assert (expected_result == actual_result), f"expected {expected_result}, got {actual_result}"
#
# - Выше решение задачи: просто сравнить значения и вывести сообщение об ошибке


# -- Задание: составные сообщения об ошибках и поиск подстроки --
# Вам дан шаблон для функции test_substring, которая принимает два значения: full_string и substring.
# Функция должна проверить вхождение строки substring в строку full_string
# с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке.
# Sample Input 1: fulltext some_value
# Sample Output 1: expected 'some_value' to be substring of 'fulltext'
# Sample Input 2: 1 1
# Sample Output 2:
# Sample Input 3: some_text some
# Sample Output 3:
#
# def test_substring(full_string, substring):
#    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
#
# - Выше решение задачи


