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
def about_game():
    os.system('cls||clear')
    print("Text about Game")
    i = input()
    if not i:
        lets_go()
    else:
        lets_go()
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
    print("Тебе дорогу пересек " + str(mob_rend_name()) + " c " + str(mob_life()) + " очками жизни")
    agr = input("Атаковать? y/n ")
    mob_life_attak = int(mob_life())
    if agr =="y" or not agr:
        print("\nТы напал на " + str(mob_name())+"a")
        while mob_life_attak >=0:
            print ("Очки жизни "+ str(mob_name()) + "а: " + str(mob_life_attak))
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
