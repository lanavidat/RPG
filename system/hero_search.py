import os

def hero_search():
    os.system('cls||clear')
    from system.hello import line
    line()
    do = " Ты решил прорядить популяцию монстров "
    print( '{0:~^80}' .format(do.upper()))
    line()
    from system.hero_mob_attack import hero_mob_attack
    hero_mob_attack()
