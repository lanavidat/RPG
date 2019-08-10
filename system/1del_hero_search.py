import os


# инициализайия поиска нового врага + шапка

def hero_search():
    os.system('cls||clear')
    from system.hello import line
    from system.hero_hit import max_hero_hit
    from system.hero.hero_info import agility, strenght, life, lvl, exper, next_lvl

    line()
    do = " Ты решил прорядить популяцию монстров "
    char = " Hit: < {}hp, ag: {} str: {}, life: {}НР, lvl: {}, exp: {}/{} " .format(max_hero_hit(), agility(), strenght(), life(), lvl(), exper(), next_lvl())


    print( '{0:~^80}' .format(do.upper()))
    print('{:~^80}'.format(char.upper()))
    line()
    from system.hero_mob_attack import hero_mob_attack
    hero_mob_attack()