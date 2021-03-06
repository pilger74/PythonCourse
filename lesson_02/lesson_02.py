##
# Домашняя работа 02:
#- Вводим с консоли число от 0 до 1000. Выводим меньшуюи большую цифру числа. (Пример: 15 => 1 -меньшая, 5 - большая)
#- Нужно хранить соответствие месяцу порядкового номера от 0 до 11. С консоли вводим либо номер месяца от 0 до 11 => получаем название месяца, вводим название месяца => получаем порядковый номер месяца
#- Возьмите любой текст из книги, в котором есть побольше знаков. Привести все слова к нижнему регистру. Составьте свое соответствие знака препинания и слова (например “.” => “[dot]” и тд). Замените все знаки в тесте на их представление. Получить частоту вхождения в текст каждого слова (включая представления знаков). Составить представление текста вида слово => список номеров слова в тексте (Пример: “мама мыла мама” => “мама”: [0,2])
#
# Задание 1
# Вводим с консоли число от 0 до 1000. Выводим меньшуюи большую цифру числа. (Пример: 15 => 1 -меньшая, 5 - большая)
min_num = 0
max_num = 1000
# Получаем значение с консоли и проверяем на корректность
while(True):
    input_num = input('Please input number (range %d .. %d)' % (min_num, max_num))
    num = int(input_num)
    if (num >= min_num) or (num <= max_num):
        break
    else:
        print('Error: incorrect number, please input correct number (range %d .. %d.')
# Цикл по строке, с поиском наименьшей и наибольшей цифры
low = input_num[0]
high = input_num[0]
for i in range(len(input_num)):
    if input_num[i] < low:
        low = input_num[i]
    if input_num[i] > high:
        high = input_num[i]
print('Find digits: low=%s, high=%s' % (low, high))

# Задание 2
# Нужно хранить соответствие месяцу порядкового номера от 0 до 11.
# С консоли вводим либо номер месяца от 0 до 11 => получаем название месяца,
# вводим название месяца => получаем порядковый номер месяца
list_months = ('январь', 'февраль', 'март',
               'апрель', 'май', 'июнь',
               'июль', 'август', 'сентябрь',
               'октябрь', 'ноябрь', 'декабрь'
              )
# Зпарос ввода с консоли номера или названия месяца, с проверкой
while(True):
    input_str = input('Введите номер (0 .. 11) или название месяца на Русском языке:')
    input_str = input_str.lower()
    # Используем особенности ленивого if
    if (input_str in list_months) or (input_str.isdecimal() and int(input_str) >= 0 and  int(input_str) <= 11):
        break
    else:
        print('Ошибка ввода данных.')
# Инициализация dict-а {Имя, Индекс} для поиска по названию
dict_months = {}
for i, val in enumerate(list_months):
    dict_months[val] = i
# Для поиска наименования месяца будкем использовать list_months
# Получение результата, в зависимости от того, что ввели, номер или название месяца
if input_str.isdecimal():
    index_month = int(input_str)
    print('Выбран месяц "%s" с порядковым номером %d' % (list_months[index_month], index_month))
else:
    print('Выбран месяц "%s" с порядковым номером %d' % (input_str, dict_months[input_str]))

# Задание 3
# Возьмите любой текст из книги, в котором есть побольше знаков.
# Привести все слова к нижнему регистру.
# Составьте свое соответствие знака препинания и слова (например “.” => “[dot]” и тд).
# Замените все знаки в тесте на их представление.
# Получить частоту вхождения в текст каждого слова (включая представления знаков).
# Составить представление текста вида слово => список номеров слова в тексте (Пример: “мама мыла мама” => “мама”: [0,2])
src_text = ''' 
"Мой дядя самых честных правил,
Когда не в шутку занемог,
Он уважать себя заставил -
И лучше выдумать не мог;
Его пример другим наука,
Но, Боже мой, какая скука
С больным сидеть и день, и ночь,
Не отходя ни шагу прочь!
Какое низкое коварство
Полуживого забавлять, 
Ему подушки поправлять, 
Печально подносить лекарство,
Вздыхать и думать про себя:
Когда же чёрт возьмёт тебя!" -
Так думал молодой повеса,
Летя в пыли на почтовых,
Всевышней волею Зевеса
Наследник всех своих родных.
Друзья Людмилы и Руслана!
С героем моего романа
Без предисловий сей же час
Позвольте познакомить вас:
Онегин, добрый мой приятель,
Родился на брегах Невы,
Где, может быть, родились Вы,
Или блистали, мой читатель!
Там некогда гулял и я,
Но вреден север для меня.
'''
# словарь символов
dict_chars = {
'\'': ' [quote] ',
'~': ' [tilde] ',
'!': ' [bang] ',
'@': ' [at] ',
'#': ' [sharp] ',
'$': ' [dollar] ',
'%': ' [percent] ',
'^': ' [caret] ',
'&': ' [ampersand] ',
'*': ' [star] ',
'(': ' [openp] ',
')': ' [closep] ',
'-': ' [minus] ',
'_': ' [underscore] ',
'=': ' [equals] ',
'+': ' [plus] ',
'{': ' [openf] ',
'}': ' [closef] ',
';': ' [semicolon] ',
':': ' [colon] ',
'\'': ' [apostrophe] ',
'\"': ' [quote] ',
',': ' [comma] ',
'.': ' [dot] ',
'/': ' [forwardslash] ',
'<': ' [less than] ',
'>': ' [greaterthan] ',
'?': ' [question] ',
'\\': ' [backslash] ',
'|': ' [pipe] ',
'§': ' [section] '
}
# получим текст c нашим обозначением символов
dst_text = src_text.replace('\n','').replace('\r', '').lower()
for c in dict_chars:
    dst_text = dst_text.replace(c, dict_chars[c])
print('Текст c нашим обозначением символов:')
print(dst_text)
# Посчитаем частоту вхождений слов, и символов из словаря
word_freq = {}
list_words = dst_text.split(' ')
for i in list_words:
    if i != '':
        word_freq[i] = word_freq.get(i, 0) + 1
print('Частота вхождений слов, и символов из словаря:')
print(word_freq)
# Составим представление текста вида слово => список номеров слова в тексте (Пример: “мама мыла мама” => “мама”: [0,2])
word_lines = {}
for i, w in enumerate(list_words):
    if (word_lines.get(w, 0) == 0):
        if w == '':
            continue
        if not ((' '+ w +' ') in dict_chars.values()):
            word_lines[w] = [i]
    else:
        word_lines[w].append(i)
print('слово => список номеров слова в тексте:')
print(word_lines)
