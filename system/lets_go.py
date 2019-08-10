import os
import sys

def exit():
    os.system('cls||clear')
    sys.exit()


# инициализайия поиска нового врага + шапка 

def hero_search():
    os.system('cls||clear')
    from system.hello import line
    from system.hero_hit import max_hero_hit
    from system.hero.hero_info import agility, strenght, life, lvl, exper, next_lvl
    from system.hero.hero_info import hero_name
    h = hero_name()  
   
    line()
    do = " " + str(h) + " решил прорядить популяцию монстров "
    char = " Hit: < {}hp, ag: {} str: {}, life: {}НР, lvl: {}, exp: {}/{} " .format(max_hero_hit(), agility(), strenght(), life(), lvl(), exper(), next_lvl())


    print( '{0:~^80}' .format(do.upper()))
    print('{:~^80}'.format(char.upper()))
    #line()
    from system.hero_mob_attack import hero_mob_attack
    hero_mob_attack()    

def lets_go():
    os.system('cls||clear')

    #print("##### TEST #####\n\n\n")                           ###### ТЕСТОВЫЙ ПОЛИГОН ######
   







    #print("\n\n\n##### TEST #####\n\n\n")   
                            ##############################

    from system.hello import line
    from system.hero.hero_info import hero_name
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
        from system.hero_stat import hero_stat
        hero_stat()

    elif lets_go_go == "3":
        from system.admin_panel import admin_panel
        admin_panel()
    elif lets_go_go == "0":
        from system.about_game import about_game
        about_game()

    else:
        print("Герой в замешательстве вертит головой\n")
        lets_go()