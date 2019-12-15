# from system.structure.admin_panel.admin_menu.admin_menu_main import

def admin_menu_main():

    print("Настройка Героя: 1\n\
Настройка Мира: 2\
\n------------------\n\
Cheate Mode: 3\
\n------------------\n\
Выйти в главное меню: 0")

    #запрос на действие в главном меню
    go = input("\nЧто сделать? ")

    # редактировать гг
    if go == "1":
        #configure_of_hero()
        pass
    # редактировать мир
    elif go == "2":
        #data_base()
        pass
    # переход в Cheate Mode
    elif go == "3":
        #cheat_mode()
        pass
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
        #admin_panel()
        pass