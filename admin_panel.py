
def admin_panel():
    do = " ADMIN PANEL "
    print("{0:~^80} \nОбнулить характеристики героя: 1\nСброс класса персонажа: 2\nВыбрать нового имени для ГГ: 3\n\
Работа с базой: 4\n\
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
        pass
    elif go == "3":
        pass
    elif go == "4":
        mob_name_base()
    else:
        print("Ой, промазал... Осторожно...\n")
        admin_panel()

# Просмотр и изменение базы имен мобов        
def mob_name_base():
    name = open("system/hero/mob_names.txt", "r").read()
    print("\nТекущие имена мобов в базе:\n" + str(name))
    admin_panel()
