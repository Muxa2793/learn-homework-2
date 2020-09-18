'''
    Создайте список словарей:

            [
            {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
            {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]

    Запишите содержимое списка словарей в файл в формате csv

'''

import csv

def main():
    profile_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}, 
    ]

    print(profile_list)    

    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        
        for profile in profile_list:
            writer.writerow(profile)


if __name__ == "__main__":
    main()