import random

# import HERO info
from system.hero.hero_info import *

# import MOB info
from system.mob.mob_info import *

mob_hp_now = 0


# сохранение рендомного значение НР в новую переменную
def mob_hp():
    return mob_hp_now


# генерация уровня НР
def random_mob_hp():
    mob_hp_life = mob_life()
    mob_lv = mob_lvl()
    h_life = life()

    # max mob life
    mob_max_hp = ((int(mob_lv) * int(mob_hp_life)) + (int(h_life) * 1.2))
    # print(mob_max_hp)
    # min mob life
    mob_min_hp = (mob_max_hp % 3) + 1
    # random mob life from min to max
    global mob_hp_now
    mob_hp_now = random.randint(mob_min_hp, mob_max_hp)
    return mob_hp_now
