import random
import sys
import os

# import HERO info
from system.hero.hero_info import *
from system.hero.hero_quantity_mob import *
from system.hero.mob_name import *

#import MOB info
from system.mob.mob_info import *

# import SYSTEM info
from admin_panel import admin_panel
from about_game import about_game

################################# Рендомный уровень НР моба #######
mob_hp_now = 0
# сохранение рендомного значение НР в новую переменную
def mob_hp():
    return mob_hp_now
# генерация уровня НР
def random_mob_hp():
    mob_hp_life = mob_life()
    mob_lvl = 15
        #max mob life
    mob_max_hp = int(mob_lvl) * int(mob_hp_life)
    #print(mob_max_hp)
        #min mob life
    mob_min_hp = mob_max_hp % 3
        #random mob life from min to max
    global mob_hp_now
    mob_hp_now = random.randint(mob_min_hp, mob_max_hp)
    return mob_hp_now
###########################################################################






# CLI-RPG
def line():
    print( '{0:~^80}' .format("~"))

def hello():
    os.system('cls||clear')
    line()
    line()
    hello_world = " Добро пожаловать в Лабиринты. Опасность ждет тебя! Будь осторожен! "
    print( '{0: ^80}' .format(hello_world).upper())
    line()
    line()
    print("{: ^80}".format("Начнем изучение нового мира!\n"))
    a = input()
    if not a:
        lets_go()
    else:
        lets_go()


####################### Info about GAME ##########################################
# import fropm about_game.py
##################################################################################

######################### Характеристика моба ####################################
#import from syste/mob/mob_char.py
##################################################################################

######################### Харакетеристика героя ##################################
# move to system/hero/hero_info
##################################################################################

######################## Randome name of Monsters ################################
# move to system/hero/mob_name
##################################################################################

######################## Ramdome mobs name #######################################
# move to system/hero/mob_name import
##################################################################################

######################## блок изменение счетчика убийства мобов ##################
# move to system/hero/hero_quantity_mob import
##################################################################################

#################### характеристики Героя по запросу #############################
# import from system/hero/....
##################################################################################

########################## Admin PANEL ###########################################
# import function from admin_panel.py
##################################################################################

def hero_stat():
    os.system('cls||clear')
    line()
    go = " Твои характеристики: "
    print("{:~^80} \nЛовкость: {}\nСила: {}\nУровень жизни: {}\nУровень героя: \
{}\nТекущий опыт: {}\nОпыт до следующего уровня: {}\nКоличество убитых монстров: \
{}\n".format(go.upper(), agility(), strenght(), life(), lvl(), exper(), next_lvl(), quantity_mob()), end=" ")
    a = input("\nИдем дальше...")
    if a or not a:
        lets_go()
    else:
        hero_stat()



###################### Система нападения на монста #################################
def hero_mob_attak():
    # приветствие с показание к-во жизни моба
    print("Тебе дорогу пересек " + str(mob_rand_name()) + " c " + str(random_mob_hp()) + " очками жизни")
    agr = input("Атаковать? y/n ")
    # пересохранение mob_hp в новую переменную
    mob_life_attak = mob_hp()

    #нападение
    if agr =="y" or not agr:
        print("\nТы напал на " + str(mob_name())+"a")
        while mob_life_attak >=0:
            #print ("Очки жизни "+ str(mob_name()) + "а: " + str(mob_life_attak))
            global strenght
            s = int(strenght())
            mob_life_attak -= s
            if mob_life_attak == 0:
                print("     {0} убит. \n\nБольше {0} не будет пугать местных селянок!! \n".format(mob_name()))
                hero_quantity_mob()
                i = input("Продолжаем геноцид? y/n: ")
                if i == "y" or not i:
                    hero_search()
                else:
                    lets_go()
    else:
        #uklon()
        lets_go()


############################## Запуск сценария атаки ############################
def hero_search():
    os.system('cls||clear')
    line()
    go = " Ты решил прорядить популяцию монстров "
    print("{:~^80}".format(go.upper()))
    hero_mob_attak()

############### Инициализация игры, вопрос "куда идем" ###########################
def lets_go():

        
 



    
    os.system('cls||clear')
    line()
    do = " Что будешь делать? "
    print("{0:~^80} \nОхота на монстров: 1\nПросмотр своих статов: 2\nАдмин панель:\
 3\n-----------------\nВыйти в консоль: 9\nКуда я попал?: 0".format(do.upper()))
    else_lets_go = input("\nТвое решение: ")
    lets_go_go = str(else_lets_go)
    if lets_go_go == "1":
        hero_search()
    elif lets_go_go == "9":
        print("Выход из игры")
        os.system('cls||clear')
        exit()
    elif lets_go_go == "2":
        hero_stat()
    elif lets_go_go == "3":
        admin_panel()
    elif lets_go_go == "0":
        about_game()

    else:
        print("Герой в замешательстве вертит головой\n")
        lets_go()


        
################# Start Game ###################################################
hello()
################################################################################

############################### EXIT ###########################################         
def exit():
    os.system('cls||clear')
    sys.exit()
################################################################################
