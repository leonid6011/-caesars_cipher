def replace_letter_right(letter, alphabet):
    index_val = alphabet.index(letter)
    if index_val + number + 1 > len(alphabet):
        index_val = index_val + number - len(alphabet)
        return alphabet[index_val]
    else:
        return alphabet[index_val + number]


def replace_letter_left(letter, alphabet):
    index_val = alphabet.index(letter)
    if index_val + number + 1 < 0:
        index_val = index_val + len(alphabet) + number
        return alphabet[index_val]
    else:
        return alphabet[index_val + number]


def alphabet_rep(string):
    number_str = len(string)
    new_string = ''
    i = 0
    while i != number_str:
        if string[i] in lower_alphabet:
            if number >= 0:
                new_string += replace_letter_right(string[i], lower_alphabet)
            else:
                new_string += replace_letter_left(string[i], lower_alphabet)
        elif string[i] in upper_alphabet:
            if number >= 0:
                new_string += replace_letter_right(string[i], upper_alphabet)
            else:
                new_string += replace_letter_left(string[i], upper_alphabet)
        else:
            new_string += string[i]
        i += 1
    return new_string


flag_alpha = True
while flag_alpha:
    print('Укажите язык алфавита: английский (eng) / русский (rus)')
    language = input()
    if language == 'eng':
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        flag_alpha = False
    elif language == 'rus':
        lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        flag_alpha = False
    else:
        print('Некоректрый ввод! Попробуйте снова')
flag_dir = True
while flag_dir:
    print('Укажите направление шифрования: влево (l) / вправо (r)')
    direction = input()
    if direction == 'l':
        flag_direction = False
        flag_dir = False
    elif direction == 'r':
        flag_direction = True
        flag_dir = False
    else:
        print('Некоректрый ввод! Попробуйте снова')
flag_number = True
while flag_number:
    number = input('Укажите шаг сдвига: ')
    if number.isdigit():
        number = int(number)
        flag_number = False
    else:
        print('Некоректрый ввод! Попробуйте снова')
if not flag_direction:
    number *= -1
if language == 'eng':
    while number > 26:
        number -= 26
else:
    while number > 32:
        number -= 32
s = input('Введите текст: ')
s2 = alphabet_rep(s)
print(s2)
