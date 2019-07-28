import os


def lets_go():
    os.system('cls||clear')

                            ###### ТЕСТОВЫЙ ПОЛИГОН ######



                            ##############################
    from system.hello import line
    line()
    do = " Что будешь делать? "
    print( '{0:~^80}' .format(do.upper()))
    print("{0:~^80} \n\nОхота на монстров: 1\nПросмотр своих статов: 2\nАдмин панель:\
 3\n-----------------\nВыйти в консоль: 9\nКуда я попал?: 0".format("~"))
    else_lets_go = input("\nТвое решение: ")
    lets_go_go = str(else_lets_go)
    if lets_go_go == "1":
        from system.hero_search import hero_search
        hero_search()
    elif lets_go_go == "9":
        print("Выход из игры")
        os.system('cls||clear')
        from launcher import exit
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