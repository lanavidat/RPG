# from system.definition import

import random

from system.hero_hit import hero_hit, max_hero_hit
from system.hero.hero_quantity_mob import hero_quantity_mob
from system.hero.hero_quantity_died import hero_quantity_died
from system.hero.mob_name import mob_name, mob_rand_name
from system.random_mob_hp import random_mob_hp, mob_hp
from system.mob_hit import mob_hit, max_mob_hit
from system.hero_next_lvl import hero_next_lvl
from system.hero.hero_info import agility, strenght, life, lvl, next_lvl, hero_name, hero_died, luck, quantity_mob, gold, exper

# Проверка на удачу. Чем больше уровень удачи, тем чаще будет случатся удачные события
def luck_check():
    from system.hero.hero_info import luck as luck

    luck = luck()
    luck = 100 - luck
    r1 = random.randint(0, luck)
    r2 = random.randint(0, luck)

    if r1 == r2:
        check_luck = True
        return check_luck

    else:
        check_luck = False
        return check_luck

# проверка на чит-мод
def cheat_mode_on_off():
    # проверка на чит режим
    cheat = open("system/hero/about_hero.py", "r")
    b = cheat.readline()
    a = eval(b)
    cheat_mode_on_off = a["cheat_mode"]

    if cheat_mode_on_off == 1:
        print ("{0:@<35} cheat mode ON {0:@>30}\n".format(""))
    else:
        pass
    cheat.close()

# рисует линию "-"
def line():
    print ("{:-^80}".format("-"))

# выводит полную статистику по характеритикам гг
def hero_statistics():
    cheat_mode_on_off()
    line()
    print ("Уровень жизни Героя:{: <19}{}".format("", life()))
    print ("Максимальный урон:{: <22}{}".format("", max_hero_hit()))
    line()
    short_log()
    print ("Кошель:{:<21}{}".format("", round(gold(),2)))
    line()
    print ("Всего боевых раундов:{: <27} construct".format(""))
    #print ("Mob ounds:{: <30} construct".format(""))
    print ("Количество побед:{: <25}{}".format("", quantity_mob()))
    print ("Количество смертей:{: <30}{}".format("", hero_died()))
    line()

# выводит краткую статистику по гг
def short_log():
    print ("Опыт:{: <14}{}/{}".format("", exper(),next_lvl()))
    print ("Уровень:{:<20}{}".format("",lvl()))
    line()
    print ("Сила:{:<17}{}".format("",strenght()))
    print ("Ловкость:{:<18}{}".format("",agility()))
    print ("Удача:{:<21}{}".format("",luck()))
    line()

# тестовый полигон
def test():

################################# ТЕСТОВЫЙ ПОЛИГОН #############################
    #print ("test")

    #from system.loot import new_gold_from_loot

    #new_gold_from_loot()



################################################################################

    pass
