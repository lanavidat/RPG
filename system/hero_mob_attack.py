#attak
import random



def hero_mob_attack():
    # приветствие с показание к-во жизни моба
    from system.hero.mob_name import mob_name, mob_rand_name
    from system.random_mob_hp import random_mob_hp, mob_hp
    print("\nТебе дорогу пересек " + str(mob_rand_name()))
    random_mob_hp()
    agr = input("Атаковать? y/n ")
    # пересохранение mob_hp в новую переменную
    mob_life_attack = mob_hp()

    #нападение
    if agr =="y" or not agr:
        from system.hero.mob_name import mob_name
        from system.random_mob_hp import mob_hp
        print("\nТы напал на " + str(mob_name())+ "a." + " У него " + str(mob_hp()) + "HP")
        while mob_life_attack >=0:
            # проверка функции отнятия жизни моба через принт 
            #print ("Очки жизни "+ str(mob_name()) + "а: " + str(mob_life_attack))
            from system.hero_hit import hero_hit
            s = float(hero_hit())
            mob_life_attack -= s
            if mob_life_attack <= 0:
                print("Ты победил {0}а. \n\nБольше {0} не будет пугать местных селянок!! \n".format(mob_name()))
                from system.hero.hero_quantity_mob import hero_quantity_mob
                hero_quantity_mob()
                i = input("Продолжаем геноцид? y/n: ")
                if not i:
                    from system.hero_search import hero_search
                    hero_search()
                elif i == "y":
                    hero_search()
                else:
                    from system.lets_go import lets_go
                    lets_go()
    else:
        #uklon()
        from system.lets_go import lets_go
        lets_go()