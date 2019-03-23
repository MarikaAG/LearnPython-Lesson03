#Создайте список словарей:
#        [
#        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
#        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
#        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
#    ]
#Запишите содержимое списка словарей в файл в формате csv

import csv

PEOPLE_LIST=[{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
             {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
             {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}]

#MAIN
with open('people.csv', 'w', encoding='utf-8') as csv_file:
    fields=['name','age','job']
    set_to_write=csv.DictWriter(csv_file, fields, delimiter=';')
    set_to_write.writeheader()
    for person in PEOPLE_LIST:
        set_to_write.writerow(person)

