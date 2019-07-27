import random
import sys

from system.hero.hero_info import *
from system.hero.hero_quantity_mob import *
from system.hero.mob_name import *
from admin_panel import admin_panel

#admin_panel()
# CLI-RPG
h = "~"
print( '\n{0:~^80}' .format(h))
print( '{0:~^80}' .format(h))
hello_world = " Привет искатель приключений. Опасность ждет тебя! Будь осторожен! "
print( '{0: ^80}' .format(hello_world))
print( '{0:~^80}' .format(h))
print( '{0:~^80}\n' .format(h))



#Характеристика моба
mob_agility = 1
mob_strenght = 1
mob_life = 2
mob_luck = 0
mob_exper = 0
mob_lvl = 1

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
def hero_stat():
    go = " Твои характеристики: "
    print("{:~^80} \nЛовкость: {}\nСила: {}\nУровень жизни: {}\nУровень героя: \
{}\nТекущий опыт: {}\nОпыт до следующего уровня: {}\nКоличество убитых монстров: \
{}\n".format(go.upper(), agility(), strenght(), life(), lvl(), exper(), next_lvl(), quantity_mob()), end=" ")

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
            global strenght
            s = int(strenght())
            mob_life_attak -= s
            if mob_life_attak == 0:
                print("\n{0} убит. \nБольше {0} не будет пугать местных селянок \n".format(mob_name()))
                hero_quantity_mob()
                hero_search()
    else:
        uklon()
        hero_search()

############################## Запуск сценария атаки ############################
def hero_search():
    go = " Ты решил прорядить популяцию монстров "
    print("{:~^80}".format(go.upper()))
    hero_search = input("Поискать нового монстра? y/n: ")
    if hero_search == "y":
        hero_mob_attak()
    else:
        uklon()
        lets_go()


########################## Admin PANEL ###########################################
# import function from admin_panel.py
##################################################################################

############### Инициализация игры, вопрос "куда идем" ###########################
def lets_go():
    do = " Что будешь делать? "
    print("{0:~^80} \nОхота на монстров: 1\nПросмотр своих статов: 2\nАдмин панель:\
 3\n-----------------\nВыйти в консоль: 9".format(do.upper()))
    else_lets_go = input("\nТвое решение: ")
    print("")
    lets_go_go = str(else_lets_go)
    if lets_go_go == "1":
        hero_search()
    elif lets_go_go == "9":
        print("Выход из игры")
        exit()
    elif lets_go_go == "2":
        hero_stat()
    elif lets_go_go == "3":
        admin_panel()
    else:
        print("Герой в замешательстве вертит головой\n")
        lets_go()

############################### EXIT ###########################################         
def exit():
    while True:
        sys.exit()
###############################################################################
        
################# Start Game ###################################################
lets_go()
