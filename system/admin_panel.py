import os

# ----------------------> Main menu --------------------------------------------
# админ меню
def admin_panel():

    # шапка и выбор
    os.system('cls||clear')
    print( '{0:~^80}' .format("~"))
    do = " ADMIN PANEL "
    print( '{0:!^80}' .format(do))
    print("{0:~^80} \n\nНастройка Героя: 1\n\
Настройка Мира: 2\
\n------------------\n\
Cheate Mode: 3\
\n------------------\n\
Выйти в главное меню: 0".format("~"))

    #запрос на действие в главном меню
    go = input("\nЧто сделать? ")

    # редактировать гг
    if go == "1":
        configure_of_hero()

    # редактировать мир
    elif go == "2":
        data_base()

    # переход в Cheate Mode
    elif go == "3":
        cheat_mode()

    elif go == "4":
        pass

    elif go == "5":
        pass

    elif go == "6":
        pass

    elif go == "7":
        pass

    elif go == "8":
        pass

    elif go == "9":
        pass

    # уходит в главное меню
    elif go == "0":
        from launcher import lets_go
        lets_go()

    # уходит в  Админку
    else:
        admin_panel()

# ----------------------------------< Main -------------------------------------
# ------------------------------------------------------------------------------
# -----------------------> Hero menu -------------------------------------------
def configure_of_hero():

    # шапка и выбор
    os.system('cls||clear')
    print( '{0:~^80}' .format("~"))
    do = " ADMIN PANEL "
    print( '{0:!^80}' .format(do))
    print("{0:~^80} \n\nОбнулить характеристики героя: 1\nСброс класса персонажа: 2\n\
Выбрать нового имени для ГГ: 3\nПросмотр текущих характеритик ГГ: 4\n\
------------------\n\
Выйти в админку: 9\n\
Выйти в главное меню: 0".format("~"))
    #
    go = input("\nЧто сделать? ")

# сброс характеристик героя из файла hero_char
    if go == "1":
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
        next = input("Имя героя изменено, теперь тебя зовут- " + str(new_name.title()))

        # уходит в админ панель при любом действии
        if not next:
            admin_panel()
        else:
            admin_panel()

    # Просмотр характеристик гг
    elif go == "4":

        # шапка и выбор
        os.system('cls||clear')
        from system.hello import line

        line()
        info = " Твои характеристики: "
        print ("{0:^80}".format(info.upper()))
        line()
        from system.definition import hero_statistics
        hero_statistics()

        i = input("\nПродолжим ...")

        # уходит в админ панель при любом действии
        if not i:
            configure_of_hero()
        else:
            configure_of_hero()

    elif go == "5":
        pass

    elif go == "6":
        pass

    elif go == "7":
        pass

    elif go == "8":
        pass

    #   переход в админку
    elif go == "9":
        admin_panel()

    # уходит в главное меню
    elif go == "0":
        from launcher import lets_go
        lets_go()

    # уходит в  Админку
    else:
        admin_panel()

# -----------------------< Hero menu -------------------------------------------
# ------------------------------------------------------------------------------
# --------------------------------> Mobs&Module menu --------------------------------
# Просмотр и изменение базы имен мобов
def data_base():

    # шапка и выбор
    os.system('cls||clear')
    i = " Настройка Мира "
    print( '{0:~^80}' .format("~"))
    print( '{0:!^80}' .format(i.upper()))
    print("{:~^80} \n\nПосмотреть все доступные имена мобов: 1\nДобавить нового моба: 2\nОткорректировать имеющееся имя: 3\
\n-------------------\nАктивные модули: 4\nВключить/выключить модули: 5\
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

    elif go == "2":
        pass

    elif go == "3":
        pass

    elif go == "4":
        check_module()

    elif go == "5":
        on_off_module()

    elif go == "6":
        pass

    elif go == "7":
        pass

    elif go == "8":
        pass

    elif go == "9":
        admin_panel()

    elif go == "0":
        from launcher import lets_go
        lets_go()

# --------------------------------< Module menu --------------------------------


#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#   !!!!!!!!!!!!!!!!!! ФУНКЦИИ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# --------------------------------> #3.0 CHEAT MODE ----------------------------
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
        next = input(" ")

        if not next:
            admin_panel()
        else:
            admin_panel()

    # Выключение читмод
    elif go_cheat == "2":
        cheat_mode_off()
        next = input(" ")

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

#
def cheat_mode_on():
    from system.modules import module_cheat_mode_launcher
    module_cheat_mode_launcher()

# Выключение чит режима
def cheat_mode_off():
    from system.modules import module_cheat_mode_off

    module_cheat_mode_off()
# --------------------------------- < Cheat Mode function ----------------------
# ------------------------------------------------------------------------------
# -------------------> Function of Module --------------------------------------

#  Проверка включеных модулей
def check_module():
    module = open("system/list_of_modules.py", "r")
    b = module.readline()
    a = eval(b)
    module_wallet_on = a["module_wallet"]
    module_gold_on = a["module_gold"]
    module_statistics_on = a['module_more_statistics']
    module_loot_on = a['module_loot']
    module_expended_statics_on = a['module_expended_statics']
    module_test_on = a['module_test']
    cheat_mode_on = a['cheat_mode']


    # проверка на включение моделя денег
    def module_cash_switch():
        if module_wallet_on == 1 and module_gold_on == 1:
            print ("Модуль денег включен")
        else:
            print("> Модуль денег не активен".upper())

    # проверка на включенность модуля для доп.статистики
    def module_statistics_switch():
        if module_statistics_on == 1:
            print ("Модуль расширенной статистики включен")
        else:
            print("> Модуль расширенной статистики не активен".upper())

    # проверка на включенность модуля для доп.статистики
    def module_loot_switch():
        if module_loot_on == 1:
            print ("Модуль лута включен")
        else:
            print("> Модуль лута не активен".upper())

    # проверка на включенность модуля TEST place
    def module_test_switch():
        if module_test_on == 1:
            print ("Модуль тестового полигона включен")
        else:
            print("> Модуль тестового полигона не активен".upper())

    # проверка на включенность модуля TEST place
    def module_expended_statics_switch():
        if module_expended_statics_on == 1:
            print ("Модуль дополнительной информации во время боя включен")
        else:
            print("> Модуль дополнительной информации во время боя не активен".upper())

    # проверка на включенность модуля CHEAT 
    def module_cheat_mode_switch():
        if cheat_mode_on == 1:
            print ("Модуль CHEAT включен")
        else:
            print("> Модуль CHEAT не активен".upper())

        module.close()

    os.system('cls||clear')
    print ("Проверка включенных модулей\n")
    module_cash_switch()
    module_loot_switch()
    module_statistics_switch()
    module_test_switch()
    module_expended_statics_switch()
    module_cheat_mode_switch()

    i = input("\nПродолжим ...")

    # уходит в админ панель при любом действии
    if not i:
        data_base()
    else:
        data_base()

# включить/выключить модуль
def on_off_module():
    os.system('cls||clear')

    print( '{0:~^80}' .format("~"))
    do = " Включить/выключить модули "
    print( '{0::^80}' .format(do))
    print( '{0:~^80}' .format("~"))

    print ("Включить модуль - 1. Выключить модуль - 0. \n\
Не изменять значение - Enter. \n\
Востановить стандартные значение - 8\n\n")

    def statistics():
        i = input ("Модуль 'Дополнительная статистика': ")
        if i == "1":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_more_statistics"] = 1
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()

            print ("Модуль 'Дополнительная статистика' активирован. Нужен перезапуск игры")
            i = input("\nПродолжим ...")

            # уходит в админ панель при любом действии
            if not i:
                input ("Не известная команда...")
                data_base()
            else:
                input ("Не известная команда...")
                data_base()

        elif i == "0":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_more_statistics"] = 0
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()
            print ("Модуль 'Дополнительная статистика' выключен. Нужен перезапуск игры")

            i = input("\nПродолжим ...")
            # уходит в админ панель при любом действии
            if not i:
                input ("Не известная команда...")
                data_base()
            else:
                input ("Не известная команда...")
                data_base()

        # уходит в админ панель при любом действии
        elif not i:
            input ("Не известная команда...")
            data_base()
        else:
            input ("Не известная команда...")
            data_base()

    def loot():
        i = input ("Модуль 'Лут': ")
        if i == "1":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_loot"] = 1
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()

            print ("Модуль 'Лут' активирован. Нужен перезапуск игры")
            statistics()

        elif i == "0":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_loot"] = 0
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()
            print ("Модуль 'Лут' выключен. Нужен перезапуск игры")
            statistics()

        elif not i:
            input ("Не известная команда...")
            statistics()
        else:
            input ("Не известная команда...")
            statistics()

    def money():
        i = input ("Модуль денег: ")
        if i == "1":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_gold"] = 1
            a['module_wallet'] = 1
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()
            print ("Модуль 'Деньги' активирован. Нужен перезапуск игры")
            loot()

        elif i == "0":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_gold"] = 0
            a['module_wallet'] = 0
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()
            print ("Модуль 'Деньги' выключен. Нужен перезапуск игры")
            loot()

        elif not i:
            input ("Не известная команда...")
            loot()
        else:
            input ("Не известная команда...")
            loot()

    

    def expended_statics():
        i = input ("Модуль дополнительной информации во время боя: ")
        if i == "1":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_expended_statics"] = 1
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()
            print ("Модуль 'дополнительной информации во время боя' активирован. Нужен перезапуск игры")
            money()

        elif i == "0":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_expended_statics"] = 0
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()
            print ("Модуль 'дополнительной информации во время боя' выключен. Нужен перезапуск игры")
            money()

        elif not i:
            input ("Не известная команда...")
            money()
        else:
            input ("Не известная команда...")
            money()

    def test():
        module_name = str('Модуль TEST')
        i = input (module_name + ": ")

        def next_module():
            expended_statics()

        if i == "1":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_test"] = 1
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()
            print (module_name + " активирован. Нужен перезапуск игры")
            next_module()

        elif i == "0":
            module = open("system/list_of_modules.py", "r")
            b = module.readline()
            a = eval(b)
            a["module_test"] = 0
            module.close()
            # запись полученного словаря(полночтью) в файл
            module = open("system/list_of_modules.py", "w")
            module.write(str(a))
            module.close()
            print (module_name + " выключен. Нужен перезапуск игры")
            next_module()

        elif not i:
            input ("Не известная команда...")
            next_module()
        else:
            input ("Не известная команда...")
            next_module()

    test()
# -------------------< Function of Module --------------------------------------
# ------------------------------------------------------------------------------
