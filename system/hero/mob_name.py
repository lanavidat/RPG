import random
######################## блок случайного имени моба ##############################
#Сохранение случайного имени моба
mob_name_h = 0
# сохранение генерации случайного имени моба
#def mob_name():
 #   return mob_name
#генерация случайного имени моба
def mob_rand_name():
    global mob_name_h
    ####### Рендомогенератор из файла
    mob_name_h = random.choice(open("system/hero/mob_names.txt", "r").read().split('\n'))
    return mob_name_h
#переменная для вывода случайного имени моба
def mob_name():
    return mob_name_h