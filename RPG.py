import random

######################## To-Do #############################
# Админ панель:
## Добавленеи новых имен в файл ./mob_name.txt
## весь код вынести в отдельный файл

# Ядро
## Создание рендомогенератора для количества сдоровья мобов
## расчет удара героя по рендомным сложениям всех параметров
## моб тоже бьет героя
### уменьшение жизни гг
## перенос параметром в отдельные файлы для записи \ чтения
## Перенос всех фенкций в отдельные файлы
## Разобратся, почему не работает относительные пути при чтении файла
## создание начисление опыта
## запись количества убитых мобов в файл
## вывод к-во убитых мобов из файла

#GIT
## Разобраться, наконецто с гитом

##############################################################

#gamer CLI-RPG
hello_world = " Привет искатель приключений. Опасность ждет тебя! Будь осторожен! "
print( '\n{0:~^80}\n' .format(hello_world))


#Харакетеристика героя
agility = 1
strenght = 1
life = 10
luck = 1
exper = 0
lvl = 1
next_lvl = 10
#quantity_mob = 0
gold = 0

#Характеристика моба
mob_agility = 1
mob_strenght = 1
mob_life = 2
mob_luck = 0
mob_exper = 0
mob_lvl = 1

######################## блок случайного имени моба ############
#Сохранение случайного имени моба
mob_name_h = 0
# сохранение генерации случайного имени моба
def mob_name():
    return mob_name
#генерация случайного имени моба
def mob_rend_name():
    global mob_name_h
    ####### Рендомогенератор из файла    
    mob_name_h = random.choice(open("mob_name.txt", "r").read().split('\n'))
    return mob_name_h
#переменная бля вывода случайного имени моба
def mob_name():
    return mob_name_h 
#################################################################

######################## блок изменение счетчика убийства мобов ############
q_mob = open("mob_quantity.txt", "r").read()
quantity_mob = int(q_mob)


#начисление очков убийства мобов
def hero_quantity_mob():
    global quantity_mob
    quantity_mob += 1




#характеристики Героя по запросу
def hero_stat():
    go = " Твои характеристики: "
    print("{:~^80} \nЛовкость: {}\nСила: {}\nУровень жизни: {}\nУровень героя: {}\nТекущий опыт: {}\nОпыт до следующего уровня: {}\nКоличество убитых монстров: {}\n".format(go, agility, strenght, life,lvl, exper, next_lvl, quantity_mob))
    
    lets_go()

#Уклонение от боя с монстром
def uklon ():
    print("\nГерой уклонился от боя\n")

#Система нападения на монста
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

#Запуск сценария атаки
def hero_search():
    go = " Ты решил прорядить популяцию монстров "
    print("{:~^80}".format(go))
    hero_search = input("Поискать нового монстра? y/n: ")
    if hero_search == "y":
        hero_mob_attak()
    else:
        uklon()
        lets_go()


#Admin PANEL
def admin_panel():
    print("Admin Panel")
    lets_go()        

#Инициализация игры, вопрос "куда идем""
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

#Запуск игры        
lets_go()