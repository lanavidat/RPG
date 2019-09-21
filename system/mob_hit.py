import random


# расчет удара моба по герою
def mob_hit():
    from system.hero.hero_info import lvl
    from system.mob.mob_info import mob_agility, mob_strenght
    m_s = float(mob_strenght())
    m_a = float(mob_agility())
    h_l = lvl()


    r = float((m_s / 1.5) + (m_a / 2.5) + (h_l / 3))
    r2 = round(r, 2)
    y = random.uniform(0,r2)
    return y

#расчет максимального удара моба по герою
def max_mob_hit():
    from system.mob.mob_info import mob_agility, mob_strenght
    from system.hero.hero_info import lvl
    m_s = float(mob_strenght())
    m_a = float(mob_agility())
    h_l = lvl()

    r = round(float((m_s / 1.5) + (m_a / 2.5) + (h_l / 3)), 2)
    return r
    print(r)
