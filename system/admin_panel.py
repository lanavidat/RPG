
import os
def admin_panel():
    #админ меню
    os.system('cls||clear')
    print( '{0:~^80}' .format("~"))
    do = " ADMIN PANEL "
    print( '{0:!^80}' .format(do))
    print("{0:~^80} \n\nОбнулить характеристики героя: 1\nСброс класса персонажа: 2\nВыбрать нового имени для ГГ: 3\n\
------------------\n\
Работа с базой: 4\n\
------------------\nВыйти в главное меню: 9".format("~"))

    go = input("\nЧто сделать? ")
    if go == "9":
        from launcher import lets_go
        lets_go()
        # сброс характеристик героя из файла hero_char
    elif go == "1":
        q = input("Точно сбросить все заслуги ГГ? (y/n): ")
        if q == "y":
            import shutil
            shutil.copy('system/hero/hero_char_replace.py', 'system/hero/hero_char.py')
            #print("\nСброс завершен...\n")
            i = input("\nСброс завершен... ")
            if not i:
                admin_panel()
            else:
                admin_panel()
        else:
            print("1")
            admin_panel()
    elif go == "2":
        admin_panel()
        pass
    elif go == "3":
        admin_panel()
        pass
    elif go == "4":
        mob_name_base()
    else:
        admin_panel()

# Просмотр и изменение базы имен мобов        
def mob_name_base():
    os.system('cls||clear')
    i = " Работа с базой имен монстров "

    print( '{0:~^80}' .format("~"))
    print( '{0:!^80}' .format(i.upper()))
    print("{:~^80} \n\nПосмотреть все доступные имена мобов: 1\nДобавить нового моба: 2\nОткорректировать имеющееся имя: 3\
\nПросмотр текущих характеритик ГГ: 4\
\n-------------------\nВыйти в Админку: 9\nВыйти в начало игры: 0\n".format("~"))
    go = input("\nЧто делаем? ")
    if go == "1":
        os.system('cls||clear')
        name = open("system/hero/mob_names.txt", "r").read()
        print("Текущие имена мобов в базе:\n\n" + str(name))
        i = input("\nПродолжить... ")
        if not i:
            mob_name_base()
        else:
            mob_name_base()
    elif go == "2":
        mob_name_base()
    elif go == "3":
        mob_name_base()
    elif go == "4":
        from system.hero_stat import hero_stat 
        os.system('cls||clear')
        from system.hero.hero_info import agility, strenght, life, lvl, exper, next_lvl, quantity_mob
        from system.hero_hit import hero_hit
        from system.hello import line
        line()
        line()
        go = " Твои характеристики: "
        print("{:~^80} \n\nУрон героя: {}\n\nЛовкость: {}\nСила: {}\nУровень жизни: {}\nУровень героя: \
{}\nТекущий опыт: {}\nОпыт до следующего уровня: {}\nКоличество убитых монстров: {}\n\
 \
\n".format("~",hero_hit(), agility(), strenght(), life(), lvl(), exper(), next_lvl(), quantity_mob()), end=" ")
        i = input("\nПродолжим ...")
        if not i:
            mob_name_base()
        else:
            mob_name_base()
    elif go == "5":
        mob_name_base()
    elif go == "6":
        mob_name_base()
    elif go == "7":
        mob_name_base()
    elif go == "8":
        mob_name_base()
    elif go == "0":
        from launcher import lets_go
        lets_go()
    elif go == "9":
        admin_panel()
    else:
        mob_name_base()
