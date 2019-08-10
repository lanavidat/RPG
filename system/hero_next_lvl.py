def hero_next_lvl():
        from system.hero.hero_info import exper, next_lvl, lvl, agility, strenght, life, lvl, exper, next_lvl, quantity_mob, luck
    # чтение количества уже убитых мобов их файла
    # чтение, сохраниене как словарь и +1 к словарю
        q_mob_read = open("system/hero/hero_char.py", "r")
        b = q_mob_read.readline()
        a = eval(b)
        lv = a["lvl"]
        i = a["exper"]
        f = a["next_lvl"]

    # Проверка на повышение уровня
        if float(i) >= float(f):
            a["lvl"] += 1
            a["next_lvl"] *= 2
            print ("{:~^80}\n\nТы получил уровень!".upper().format("~"))

    #  генератор числа для повышение характеристики        
            import random
            r = random.random()
    #  если рендом до 0,2 плючика не будет
            if r < 0.2:
                print("Боги не обратили на тебя внимания. Ты не получил новых характеристик", end=" ")
    #  если рендом от 0,2 до 0,4 -- получаем +1 силы
            elif r >=0.2 and r <= 0.4:
                a["strenght"] += 1
                print ("Боги сделали тебя сильнее!")
                print("\nТвои новые характеристики: ".upper() +  "\nСила: {}".format(strenght()), end=" ")
    #  если рендом от 0,4 до 0,8 - получаем +1 ловкости
            elif r > 0.4 and r <= 0.8:
                a["agility"] += 1
                print("Боги сделали тебя более ловким!")
                print("\nТвои новые характеристики: ".upper() +  "\nЛовкость: {}".format(agility()), end=" ")
    #  если рендом от 0,8 до 0,95 получаем +10 жизни
            elif r > 0.8 and r <= 0.95:
                a["life"] += 10
                print("Боги дали тебе больше жизни!")
                print("\nТвои новые характеристики: ".upper() +  "\nЖизненые силы героя: {}".format(life()), end=" ")
    #  если рендом от 0,95 до 1,0 получаем +1 к удачи
            else:
                print("Тебе повезло! Боги будут чаще тебе улыбатся!")
                a["luck"] += 1
                print("\nТвои новые характеристики: ".upper() +  "\nУдача героя: {}".format(luck()), end=" ")

            print("\n\n{:~^80}\n".format("~"))

    #  записывает результат в файл        
            q_mob_write = open("system/hero/hero_char.py", "w")
            q_mob_write.write(str(a))
            q_mob_write.close()
            
          
        q_mob_read.close()
        # запись полученного словаря(полночтью) в файл