import os


def hero_stat():
    os.system('cls||clear')
    do = " Характеристики игрока "
    from system.hero.hero_info import agility, strenght, life, lvl, exper, next_lvl, quantity_mob, hero_died, luck
    from system.hero_hit import max_hero_hit
    print( '{0:~^80}'.format("~"))
    print( '{0:~^80}' .format(do.upper()))
    print("{:~^80} \n\nМаксимальный урон героя за раунд: {}НР\n\nЛовкость: {}\nСила: {}\nУдача: {}\nУровень жизни: {}НР\n\nУровень героя: \
{}\nТекущий опыт: {}\nОпыт до следующего уровня: {}\n\nКоличество убитых монстров: {}\n\
Количество смертей: {}\n".format("~", max_hero_hit(), agility(), strenght(), luck(), life(), lvl(), exper(), next_lvl(), quantity_mob(), hero_died()), end=" ")
    a = input("\nИдем дальше...")
    if a or not a:
        from launcher import lets_go
        lets_go()
    else:
        
        hero_stat()
