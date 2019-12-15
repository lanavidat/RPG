# from system.definition import

import random
from tqdm import tqdm
import time

from system.hero_hit import hero_hit, max_hero_hit
from system.hero.hero_quantity_mob import hero_quantity_mob
from system.hero.hero_quantity_died import hero_quantity_died
from system.hero.mob_name import mob_name, mob_rand_name
from system.random_mob_hp import random_mob_hp, mob_hp
from system.mob_hit import mob_hit, max_mob_hit
from system.hero_next_lvl import hero_next_lvl
from system.hero.hero_info import agility, strenght, life, lvl, next_lvl, hero_name, hero_died, luck, quantity_mob, gold, exper
from system.modules import module_wallet, module_cash_switch, module_more_statistics, module_loot, module_expended_statics

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
    from system.modules import module_cheat_mode_switch
    module_on = str(module_cheat_mode_switch())
    if module_on == "1":
        print ("{0:@<30} cheat mode ON {0:@>35}".format(""))
    else:
        pass


# рисует линию "-"
def line():
    print ("{:-^80}".format("-"))

# выводит полную статистику по характеритикам гг
def hero_statistics():
    cheat_mode_on_off()
    line()
    print ("Количество жизни Героя:{: <19}{}".format("", life()))
    print ("Максимальный урон:{: <22}{}".format("", max_hero_hit()))
    line()
    short_log()
    module_wallet()
    module_more_statistics()
    module_loot()

# выводит краткую статистику по гг
def short_log():
    line()
    from system.modules import module_expended_statics
    module_expended_statics_on = module_expended_statics()



    print ("Уровень и опыт:{}({}/{}) | ".format(lvl(),exper(),next_lvl()),end=" ")
    print ("Сила:{} | Ловкость:{} | Удача:{} ".format(strenght(), agility(), luck()))
    if module_expended_statics_on == 1:
        pass

    line()

# тестовый полигон
def test():
    from system.modules import module_test
    mt_on = module_test()
    if mt_on == 1:
        print ("module test on".upper())
 ################################# ТЕСТОВЫЙ ПОЛИГОН #############################
        #from system.loot import new_gold_from_loot


 ################################# ТЕСТОВЫЙ ПОЛИГОН #############################

################################################################################

        
