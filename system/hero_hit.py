import random


# расчет удара героя на моба
def hero_hit():
    from system.hero.hero_info import agility, strenght, luck, lvl
    s = float(strenght())
    a = float(agility())
    l = float(luck())
    l = lvl()


    r = float((s / 2) + (a / 5) + (l / 3))
    r2 = round(r, 2)
    y = random.uniform(0,r2)
    return y

    
# расчет максимального удара героя по мобу
def max_hero_hit():
    from system.hero.hero_info import agility, strenght, luck, lvl
    s = float(strenght())
    a = float(agility())
    l = float(luck())
    l = lvl()

    r = round(float((s / 2) + (a / 5) + (l / 3)), 2)
    return r
