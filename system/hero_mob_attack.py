#attak
import random

def hero_mob_attack():
    from system.hero_hit import hero_hit, max_hero_hit
    from system.exper import new_exp, exper
    from system.hero.hero_quantity_mob import hero_quantity_mob
    from system.hero.hero_quantity_died import hero_quantity_died
    from system.hero.hero_info import life
    from system.hero.mob_name import mob_name, mob_rand_name
    from system.random_mob_hp import random_mob_hp, mob_hp
    from system.hero.mob_name import mob_name
    from system.random_mob_hp import mob_hp


    print("\nТебе дорогу пересек " + str(mob_rand_name()))
    random_mob_hp()
    agr = input("Атаковать? y/n ")
    # пересохранение mob_hp в новую переменную
   # mob_life_attack = mob_hp()

    def combat():
        global mob_life_attack
        global hero_life
        global max_hero_hits
        max_hit = max_hero_hit()
        
        #hero_hits = round(hero_hit(), 2)
        print("Максимальный урон героя: " + str(max_hit) + "HP")
        hero_life = float(life())
        print("Уровень жизни героя " + str(hero_life))
        mob_life_attack = float(mob_hp())
        print("Уровень жизни " + str(mob_name()) + "a: " + str(mob_life_attack) + "\n")

        while True:
            hero_hits = round(hero_hit(), 2)
            from system.hero_search import hero_search
            hero_random = random.random()
            #print ("hero random " + str(hero_random))
            mob_random = random.random()
            #print ("mobs random " + str(mob_random))
            
            if hero_random >= mob_random:

                         
                mob_life_attack -= hero_hits
                int_mob_life = round(mob_life_attack, 2)
                    
                print("Герой лупит со всей силы, на " + str(hero_hits) + "НР. В " +str(mob_name()) + "a осталось " + str(int_mob_life) + "HP")
                
                if int_mob_life <= 0:
                    i = "\nТы победил "
                    print(str(i.upper()) + "{0}A.".format(mob_name().upper(), mob_name()))
                    print("\nПобеда над {0}ом принесла герою опыт в размере - {1} ед.\n".format(mob_name(), float(exper())))
                     # зачисление еденичку за убийство
                    hero_quantity_mob()
                # геноцидим дальше?
                    i = input("Продолжаем геноцид? y/n: ")
                    if not i:
                        from system.hero_search import hero_search
                        hero_search()
                    elif i == "y":
                        hero_search()
                    else:
                        from system.lets_go import lets_go
                        lets_go()
                #combat()

              
            if hero_random <= mob_random:
               # удар моба
                hero_life -= 1
                int_hero_life = round(hero_life, 2)
                
                print("     " + str(mob_name()) + " ударил героя. Жизнь героя:  " + str(int_hero_life) + "HP")
                #combat()
                if int_hero_life <= 0:
                    print("\nГерой погиб не выдержав побоев.\n".upper())
                     # зачисление еденичку за убийство
                    hero_quantity_died()
                    i = input("Попытать счастье еще раз? y/n: ")
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

    if agr =="y" or not agr:
        from system.hero.mob_name import mob_name
        from system.random_mob_hp import mob_hp
   
        print("\nТы безумно рванулся в бой!\n")
        combat()
  