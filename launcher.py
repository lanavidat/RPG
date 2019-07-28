import random
import sys
import os

# import HERO info
from system.hero.hero_info import *                 # Харакетеристика героя
from system.hero.hero_quantity_mob import *         # блок изменение счетчика убийства мобов
from system.hero.mob_name import *                  # Randome name of Monsters
from system.hero_stat import *                      # Hero stat
from system.hero_hit import hero_hit                # расчет удара ГГ по мобу

#import MOB info
from system.mob.mob_info import *
from system.random_mob_hp import *                  # Рендомный уровень НР моба
#from system.mob_char import *                       # Характеристика моба

# import SYSTEM info
from system.admin_panel import admin_panel          # Admin PANEL
from system.about_game import about_game            # Info about GAME
from system.hello import *                          # Hello


###################### Система нападения на монста #################################
def hero_mob_attak():
    # приветствие с показание к-во жизни моба
    print("\nТебе дорогу пересек " + str(mob_rand_name()))
    random_mob_hp()
    agr = input("Атаковать? y/n ")
    # пересохранение mob_hp в новую переменную
    mob_life_attak = mob_hp()

    #нападение
    if agr =="y" or not agr:
        print("\nТы напал на " + str(mob_name())+ "a." + " У него " + str(mob_hp()) + "HP")
        while mob_life_attak >=0:
            # проверка функции отнятия жизни моба через принт 
            #print ("Очки жизни "+ str(mob_name()) + "а: " + str(mob_life_attak))
            global hero_hit
            s = float(hero_hit())
            mob_life_attak -= s
            if mob_life_attak <= 0:
                print("Ты победил {0}а. \n\nБольше {0} не будет пугать местных селянок!! \n".format(mob_name()))
                hero_quantity_mob()
                i = input("Продолжаем геноцид? y/n: ")
                if not i:
                    hero_search()
                elif i == "y":
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
    do = " Ты решил прорядить популяцию монстров "
    print( '{0:~^80}' .format(do.upper()))
    line()
    hero_mob_attak()

############### Инициализация игры, вопрос "куда идем" ###########################
def lets_go():
    os.system('cls||clear')

                            ###### ТЕСТОВЫЙ ПОЛИГОН ######

    



                            ##############################
    line()
    do = " Что будешь делать? "
    print( '{0:~^80}' .format(do.upper()))
    print("{0:~^80} \n\nОхота на монстров: 1\nПросмотр своих статов: 2\nАдмин панель:\
 3\n-----------------\nВыйти в консоль: 9\nКуда я попал?: 0".format("~"))
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
################################################################################

        
################# Start Game ###################################################
hello()

################################################################################

############################### EXIT ###########################################         
def exit():
    os.system('cls||clear')
    sys.exit()
################################################################################
