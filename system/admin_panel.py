import os

# админ меню
def admin_panel():

    # шапка и выбор
    os.system('cls||clear')
    print( '{0:~^80}' .format("~"))
    do = " ADMIN PANEL "
    print( '{0:!^80}' .format(do))
    print("{0:~^80} \n\nОбнулить характеристики героя: 1\nСброс класса персонажа: 2\nВыбрать нового имени для ГГ: 3\n\
------------------\n\
Работа с базой: 4\nCheate Mode: 5\n\
------------------\nВыйти в главное меню: 9".format("~"))
    #
    go = input("\nЧто сделать? ")

    # выйти в главное меню
    if go == "9":
        from launcher import lets_go
        lets_go()

# сброс характеристик героя из файла hero_char
    elif go == "1":
        q = input("Точно сбросить все характерисики ГГ? (y/n): ")

        # подтверждение на обнуление характеристик
        if q == "y":
            import shutil
            shutil.copy('system/hero/hero_char_replace.py', 'system/hero/hero_char.py')
            i = input("\nСброс завершен... ")

            # уходит в админ панель при любом действии
            if not i:
                admin_panel()
            else:
                admin_panel()
        # уходит в админ панель
        else:
            admin_panel()

    # выбрать класс для ГГ
    elif go == "2":
        admin_panel()

    # Change Hero name
    elif go == "3":

        # установка нового имени на основе введеного
        new_name = input("Новое имя героя: ")
        show_name = open("system/hero/about_hero.py", "r")
        b = show_name.readline()
        a = eval(b)
        a["hero_name"] = new_name
        show_name.close()

        # запись полученного словаря(полночтью) в файл
        name_write = open("system/hero/about_hero.py", "w")
        name_write.write(str(a))
        name_write.close()
        next = input("Имя героя изменено, теперь тебя зовут " + str(new_name.title()))

        # уходит в админ панель при любом действии
        if not next:
            admin_panel()
        else:
            admin_panel()

    # редактировать DataBase
    elif go == "4":
        data_base()

    # переход в Cheate Mode
    elif go == "5":
        cheat_mode()

    # уходит в админ панель
    else:
        admin_panel()

# Просмотр и изменение базы имен мобов
def data_base():

    # шапка и выбор
    os.system('cls||clear')
    i = " Работа с базой имен монстров "
    print( '{0:~^80}' .format("~"))
    print( '{0:!^80}' .format(i.upper()))
    print("{:~^80} \n\nПосмотреть все доступные имена мобов: 1\nДобавить нового моба: 2\nОткорректировать имеющееся имя: 3\
\nПросмотр текущих характеритик ГГ: 4\
\n-------------------\nВыйти в Админку: 9\nВыйти в начало игры: 0\n".format("~"))
    go = input("\nЧто делаем? ")

    # просмотр все имена доступных мобов
    if go == "1":
        os.system('cls||clear')
        name = open("system/hero/mob_names.txt", "r").read()
        print("Текущие имена мобов в базе:\n\n" + str(name))
        i = input("\nПродолжить... ")

        # уходит в админ панель при любом действии
        if not i:
            data_base()
        else:
            data_base()

    # добавить нового моба
    elif go == "2":
        data_base()

    # Откорректировать имена имеющихся мобов
    elif go == "3":
        data_base()

    # Просмотр характеристик гг
    elif go == "4":

        # шапка и выбор
        from system.hero_stat import hero_stat
        os.system('cls||clear')
        from system.hero.hero_info import agility, strenght, life, lvl, exper, next_lvl, quantity_mob
        from system.hero_hit import hero_hit
        from system.hello import line
        line()
        line()
        go = " Твои характеристики: "

        from system.definition import hero_statistics
        hero_statistics()

        i = input("\nПродолжим ...")

        # уходит в админ панель при любом действии
        if not i:
            data_base()
        else:
            data_base()

    # c 5-8 забронированые для новых функций
    elif go == "5":
        data_base()
    elif go == "6":
        data_base()
    elif go == "7":
        data_base()
    elif go == "8":
        data_base()

    # уходит в главное меню
    elif go == "0":
        from launcher import lets_go
        lets_go()

    # уходит в админку
    elif go == "9":
        admin_panel()

    # уходит в датабазу
    else:
        data_base()

# режим чита-мода
def cheat_mode():

    # шапка и режим выбора
    os.system('cls||clear')
    a = " Cheat Mode "
    print( '{0:~^80}' .format("~"))
    print( '{0:!^80}' .format(a.upper()))
    print("{:~^80} \n\nCheat Mode ON: 1\nCheat Mode OFF: 2\n\
    \n-------------------\nВыйти в Админку: 9\nВыйти в начало игры: 0\n".format("~"))
    go_cheat = input("\nЧто делаем? ")

    # включить чит-мод
    if go_cheat == '1':
        cheat_mode_on()
        next = input("Cheat mode On ")

        if not next:
            admin_panel()
        else:
            admin_panel()

    # Выключение читмод
    elif go_cheat == "2":
        cheat_mode_off()
        next = input("Cheat mode OFF ")

        # в любом нажатии уходит в админку
        if not next:
            admin_panel()
        else:
            admin_panel()

# уходит в главменю
    elif go_cheat == "0":
        from launcher import lets_go
        lets_go()

# уходит в админку
    elif go_cheat == "9":
        admin_panel()

    # уходит в редактирование базы
    else:
        data_base()

# CHEAT MODE
def cheat_mode_on():
    cheat = open("system/hero/hero_char.py", "r")
    t = cheat.readline()
    y = eval(t)
    y["agility"] = 100
    y['strenght'] = 100
    y['life'] = 100
    cheat.close()
    # запись полученного словаря(полночтью) в файл
    cheat_mode = open("system/hero/hero_char.py", "w")
    cheat_mode.write(str(y))
    cheat_mode.close()

# изменение показателя чита-мода
    cheat = open("system/hero/about_hero.py", "r")
    b = cheat.readline()
    a = eval(b)
    a["cheat_mode"] = 1
    cheat.close()
    # запись полученного словаря(полночтью) в файл
    cheat_mode = open("system/hero/about_hero.py", "w")
    cheat_mode.write(str(a))
    cheat_mode.close()

# Выключение чит режима
def cheat_mode_off():
    import shutil
    shutil.copy('system/hero/hero_char_replace.py', 'system/hero/hero_char.py')

    cheat = open("system/hero/about_hero.py", "r")
    m = cheat.readline()
    n = eval(m)
    n["cheat_mode"] = 0
    cheat.close()
    # запись полученного словаря(полночтью) в файл
    cheat_mode = open("system/hero/about_hero.py", "w")
    cheat_mode.write(str(n))
    cheat_mode.close()
