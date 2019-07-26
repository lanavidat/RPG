import random

# CLI-RPG
h = "~"
print( '\n{0:~^80}' .format(h))
print( '{0:~^80}' .format(h))
hello_world = " Привет искатель приключений. Опасность ждет тебя! Будь осторожен! "
print( '{0: ^80}' .format(hello_world))
print( '{0:~^80}' .format(h))
print( '{0:~^80}\n' .format(h))


#Харакетеристика героя
agility = 1
strenght = 1
life = 10
luck = 1
exper = 0

next_lvl = 10
gold = 0

######################### Харакетеристика героя ###############################
#считывание к-во убитых мобов с файла 
def quantity_mob():
    q_mob_read = open("system/hero/mob_quantity.txt", "r")
    q_now = q_mob_read.read()
    return q_now
    q_mob_read.close()
# уровень героя
def lvl():
    q_mob_read = open("system/hero/hero_lvl.txt", "r")
    q_now = q_mob_read.read()
    return q_now
    q_mob_read.close()

############################################################################### 




#Характеристика моба
mob_agility = 1
mob_strenght = 1
mob_life = 2
mob_luck = 0
mob_exper = 0
mob_lvl = 1

######################## блок случайного имени моба ##############################
#Сохранение случайного имени моба
mob_name_h = 0
# сохранение генерации случайного имени моба
def mob_name():
    return mob_name
#генерация случайного имени моба
def mob_rend_name():
    global mob_name_h
    ####### Рендомогенератор из файла    
    mob_name_h = random.choice(open("system/hero/mob_name.txt", "r").read().split('\n'))
    return mob_name_h
#переменная для вывода случайного имени моба
def mob_name():
    return mob_name_h 
###################################################################################

######################## блок изменение счетчика убийства мобов ###################
def hero_quantity_mob():
    # чтение количества уже убитых мобов их файла
    q_mob_read = open("system/hero/mob_quantity.txt", "r")
    q_now = q_mob_read.read()
    plus_one = 1
    q_now = int(q_now) + int(plus_one)
    q_mob_read.close()
    # к числу полученного при чтении файла добавлем еденичку 
    q_mob_write = open("system/hero/mob_quantity.txt", "w")
    q_mob_write.write(str(q_now))
    q_mob_write.close()
####################################################################################

#################### характеристики Героя по запросу ###############################
def hero_stat():
    go = " Твои характеристики: "
    print("{:~^80} \nЛовкость: {}\nСила: {}\nУровень жизни: {}\nУровень героя: {}Текущий опыт: {}\nОпыт до следующего уровня: {}\nКоличество убитых монстров: {}\n".format(go, agility, strenght, life,lvl(), exper, next_lvl, quantity_mob()), end="")
    
    lets_go()

################3 Уклонение от боя с монстром ######################################
def uklon ():
    print("\nГерой уклонился от боя\n")

###################### Система нападения на монста #################################
def hero_mob_attak():
    print("\nТебе дорогу пересек " + str(mob_rend_name()) + " c " + str(mob_life) + " очками жизни")
    agr = input("Атаковать? y/n ")
    mob_life_attak = mob_life
    if agr =="y":
        print("\nТы напал на " + str(mob_name())+"a")
        while mob_life_attak >=0:
            print ("Очки жизни "+ str(mob_name()) + "а : " + str(mob_life_attak))
            mob_life_attak -= strenght
            if mob_life_attak == 0:
                print("{0} убит. Больше {0} не будет пугать местных селянок \n".format(mob_name()))
                hero_quantity_mob()
                hero_search()
    else:
        uklon()
        hero_search()

############################## Запуск сценария атаки ############################
def hero_search():
    go = " Ты решил прорядить популяцию монстров "
    print("{:~^80}".format(go))
    hero_search = input("Поискать нового монстра? y/n: ")
    if hero_search == "y":
        hero_mob_attak()
    else:
        uklon()
        lets_go()


########################## Admin PANEL ###########################################
def admin_panel():
    print("Admin Panel")
    lets_go()        

############### Инициализация игры, вопрос "куда идем" ###########################
def lets_go():
    do = " Что будешь делать? "
    print("{0:~^80} \nОхота на монстров: 1\nПросмотр своих статов: 2\nАдмин панель: 3\nВыйти в консоль: ex".format(do))
    else_lets_go = input("\nТвое решение: ")
    print("")
    lets_go_go = str(else_lets_go)
    if lets_go_go == "1":
        hero_search()
    elif lets_go_go == "ex":
        print("Выход")
    elif lets_go_go == "2":
        hero_stat()
    elif lets_go_go == "3":
        admin_panel()
    else:
        print("Герой в замешательстве вертит головой")
        lets_go()

################# Запуск игры ###################################################  
lets_go()