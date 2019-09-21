import os
import sys
import time

def exit():
    os.system('cls||clear')
    sys.exit()


# инициализайия поиска нового врага + шапка

def hero_search():
    os.system('cls||clear')
    from system.hello import line
    from system.hero_hit import max_hero_hit
    from system.hero.hero_info import agility, strenght, life, lvl, exper, next_lvl, hero_name
    #from system.hero.hero_info import hero_name
    #line()
    from system.hero_mob_attack import hero_mob_attack
    hero_mob_attack()

def lets_go():
    os.system('cls||clear')
    from system.hello import line
    from system.hero.hero_info import hero_name
    from system.about_game import about_game
    from system.hero_stat import hero_stat
    from system.admin_panel import admin_panel

    #print("##### TEST #####\n\n\n")                           ###### ТЕСТОВЫЙ ПОЛИГОН ######







    #print("\n\n\n##### TEST #####\n\n\n")
                            ##############################


    h = hero_name()
    do = " Приветствуем, " + str(h) + "! Что будешь делать? "
    line()
    print( '{0:~^80}'.format(do.upper()))
    print("{0:~^80} \n\nОхота на монстров: 1\nПросмотр своих статов: 2\nАдмин панель:\
 3\n-----------------\nВыйти в консоль: 9\nКуда я попал?: 0".format("~"))
    else_lets_go = input("\nТвое решение: ")
    lets_go_go = str(else_lets_go)
    if lets_go_go == "1":
        #from system.hero_search import hero_search
        hero_search()
    elif lets_go_go == "9":
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
