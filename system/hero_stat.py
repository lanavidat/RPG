import os


def hero_stat():
    os.system('cls||clear')
    do = " Характеристики игрока "
    from system.hero.hero_info import agility, strenght, life, lvl, exper, next_lvl, quantity_mob, hero_died
    from system.hero_hit import hero_hit
    print( '{0:~^80}'.format("~"))
    print( '{0:~^80}' .format(do.upper()))
    print("{:~^80} \n\nУрон героя за проход: {}\n\nЛовкость: {}\nСила: {}\nУровень жизни: {}\n\nУровень героя: \
{}\nТекущий опыт: {}\nОпыт до следующего уровня: {}\nКоличество убитых монстров: {}\n\
Количество смертей: {}\n".format("~", hero_hit(), agility(), strenght(), life(), lvl(), exper(), next_lvl(), quantity_mob(), hero_died()), end=" ")
    a = input("\nИдем дальше...")
    if a or not a:
        from launcher import lets_go
        lets_go()
    else:
        
        hero_stat()
