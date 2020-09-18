'''
Задание

    Скачайте файл по ссылке
    Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
    Подсчитайте количество слов в тексте
    Замените точки в тексте на восклицательные знаки
    Сохраните результат в файл referat2.txt
'''

import re

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        
        len_text = len(text)
        print(f'Всего символов: {len_text}')
        
        split_text = re.split("[,.«»\n: ]+", text)
        split_text = len(split_text)
        print(f'Всего слов: {split_text}')
        
        exclaim_text = text.replace('.', '!')
    
    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(exclaim_text)

if __name__ == "__main__":
    main()
