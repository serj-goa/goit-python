import re


user_string = '''Дорогие друзья, повышение уровня гражданского сознания напрямую зависит
от системы обучения кадров, соответствующей насущным потребностям. 14685430
Значимость этих проблем настолько очевидна, что постоянный количественный рост
и сфера нашей активности требует определения и уточнения дальнейших
направлений развития проекта? Дорогие друзья, курс на социально-ориентированный
национальный проект в значительной степени обуславливает создание направлений
прогрессивного развития.'''


def normalize(sentence):

    letter_dict = {ord('а'): 'a', ord('А'): 'A', ord('б'): 'b', ord('Б'): 'B',
                  ord('в'): 'v', ord('В'): 'V', ord('г'): 'g', ord('Г'): 'G',
                  ord('д'): 'd', ord('Д'): 'D', ord('е'): 'e', ord('Е'): 'E',
                  ord('ё'): 'jo', ord('Ё'): 'Jo', ord('ж'): 'zh', ord('Ж'): 'Zh',
                  ord('з'): 'z', ord('З'): 'Z', ord('и'): 'i', ord('И'): 'I',
                  ord('й'): 'y', ord('Й'): 'Y', ord('к'): 'k', ord('К'): 'K',
                  ord('л'): 'l', ord('Л'): 'L', ord('м'): 'm', ord('М'): 'M',
                  ord('н'): 'n', ord('Н'): 'N', ord('о'): 'o', ord('О'): 'O',
                  ord('п'): 'p', ord('П'): 'P', ord('р'): 'r', ord('Р'): 'R',
                  ord('с'): 's', ord('С'): 'S', ord('т'): 't', ord('Т'): 'T',
                  ord('у'): 'u', ord('У'): 'U', ord('ф'): 'f', ord('Ф'): 'F',
                  ord('х'): 'h', ord('Х'): 'H', ord('ц'): 'ts', ord('Ц'): 'Ts',
                  ord('ч'): 'ch', ord('Ч'): 'Ch', ord('ш'): 'sh', ord('Ш'): 'Sh',
                  ord('щ'): 'shch', ord('Щ'): 'Shch', ord('ы'): 'y', ord('Ы'): 'Y',
                  ord('ь'): '', ord('Ь'): '', ord('ъ'): '', ord('Ъ'): '',
                  ord('э'): 'e', ord('Э'): 'E', ord('ю'): 'ju', ord('Ю'): 'Ju',
                  ord('я'): 'Ja', ord('Я'): 'Ja'}
    latin_sentence = sentence.translate(letter_dict)
    result_sentence = re.sub(r'\W', "_", latin_sentence)
    return result_sentence

print(normalize(user_string))