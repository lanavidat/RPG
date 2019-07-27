
import os
def admin_panel():
    os.system('cls||clear')
    print( '{0:~^80}' .format("~"))
    do = " ADMIN PANEL "
    print( '{0:~^80}' .format("~"))
    print("{0:~^80} \nОбнулить характеристики героя: 1\nСброс класса персонажа: 2\nВыбрать нового имени для ГГ: 3\n\
\nРабота с базой: 4\n\
------------------\nВыйти в главное меню: 9\n".format(do))

    go = input("Что сделать? ")
    if go == "9":
        from launcher import lets_go
        lets_go()
    elif go == "1":
        q = input("Точно сбросить все заслуги ГГ? (y/n): ")
        if q == "y":
            import shutil
            shutil.copy('system/hero/hero_char_replace.py', 'system/hero/hero_char.py')
            print("\nСброс завершен...\n")
            admin_panel()
        else:
            print("1")
            admin_panel()
    elif go == "2":
        print("Under construct....")
        admin_panel()
        pass
    elif go == "3":
        print("Under construct....")
        admin_panel()
        pass
    elif go == "4":
        mob_name_base()
    else:
        print("Ой, промазал... Осторожно...\n")
        admin_panel()

# Просмотр и изменение базы имен мобов        
def mob_name_base():
    os.system('cls||clear')
    print( '{0:~^80}' .format("~"))
    print( '{0:~^80}' .format("~"))
    i = " Работа с базой имен монстров "
    print("{:~^80} \nПосмотреть все доступные имена мобов: 1\nДобавить нового моба: 2\nОткорректировать имеющееся имя: 3\
\n-------------------\nВыйти в начало игры: 4\nВыйти в Админку: 5".format(i.upper()))
    go = input("\nЧто делаем? ")
    if go == "1":
        name = open("system/hero/mob_names.txt", "r").read()
        print("\nТекущие имена мобов в базе:\n" + str(name))
        mob_name_base()
    elif go == "2":
        print("Under construct....")
        mob_name_base()
    elif go == "3":
        print("Under construct....")
        mob_name_base()
    elif go == "4":
        from launcher import lets_go
        lets_go()
    elif go == "5":
        admin_panel()
    else:
        mob_name_base()
