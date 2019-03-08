#Скачайте файл по ссылке
#Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt

#MAIN


with open('referat.txt', 'r', encoding='utf-8') as fl:
    fl_str=fl.read()
    fl_len=len(fl_str)
    print(f'Символов в файле: {fl_len}')
    fl_str_sp=fl_str.split()
    fl_words=len(fl_str_sp)
    print(f'Слов в файле: {fl_words}')
    fl_str2=fl_str.replace(".","!")
    #print(fl_str)
with open('referat2.txt','w',encoding='utf-8') as fl:
    fl.write(fl_str2)
    

