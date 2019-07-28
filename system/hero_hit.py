


# расчет удара героя на моба
def hero_hit():
    from system.hero.hero_info import agility, strenght, luck
    s = float(strenght())
    a = float(agility())
    l = float(luck())


    y = (s / 2) + (a / 5)
    return y

