import random


# расчет удара героя на моба
def hero_hit():
    from system.hero.hero_info import agility, strenght, luck
    s = float(strenght())
    a = float(agility())
    l = float(luck())


    r = float((s / 2) + (a / 5))
    r2 = round(r, 2)
    y = random.uniform(0,r2)
    return y

def max_hero_hit():
    from system.hero.hero_info import agility, strenght, luck
    s = float(strenght())
    a = float(agility())
    l = float(luck())

    r = float((s / 2) + (a / 5))
    return r