import os
import sys
import time

# функция выхода в консоль
def exit():
    os.system('cls||clear')
    sys.exit()

# инициализайия поиска нового врага + шапка
def hero_search():
    from system.definition import line
    from system.hero_hit import max_hero_hit
    from system.hero.hero_info import agility, strenght, life, lvl, exper, next_lvl, hero_name
    from system.hero_mob_attack import hero_mob_attack
    hero_mob_attack()
    os.system('cls||clear')

# функция отрисовки окна и выбора дальнейшего пути
def lets_go():
    os.system('cls||clear')
    from system.hero.hero_info import hero_name
    from system.about_game import about_game
    from system.hero_stat import hero_stat
    from system.admin_panel import admin_panel
    from system.definition import cheat_mode_on_off, test, line

    test()

    # шапка и выбор пути
    h = hero_name()
    do = " Приветствуем, " + str(h) + "! Что будешь делать? "
    line()

    print( '{0:~^80}'.format(do.upper()))

    # проверка на чит режим
    cheat_mode_on_off()

    print("{0:~^80} \n\nОхота на монстров: 1\nПросмотр своих статов: 2\nАдмин панель:\
 3\n-----------------\nВыйти в консоль: 9\nКуда я попал?: 0".format("~"))


    else_lets_go = input("\nТвое решение: ")
    lets_go_go = str(else_lets_go)

    # запуск охоты на мобов
    if lets_go_go == "1":
        hero_search()

    # выход в консоль
    elif lets_go_go == "9":
        os.system('cls||clear')
        exit()

    # просмотр статистику по гг
    elif lets_go_go == "2":
        hero_stat()

    # переход в админку
    elif lets_go_go == "3":
        admin_panel()

    # переход в раздел информации про игру
    elif lets_go_go == "0":
        about_game()

    else:
        print("Герой в замешательстве вертит головой\n")
        lets_go()
