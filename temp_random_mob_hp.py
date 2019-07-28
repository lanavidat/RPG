import random
import sys
import os

# import HERO info
from system.hero.hero_info import *
from system.hero.hero_quantity_mob import *
from system.hero.mob_name import *

#import MOB info
from system.mob.mob_info import *

# import SYSTEM info
from admin_panel import admin_panel
from about_game import about_game


def random_mob_hp():
    mob_hp = mob_life()
    mob_lvl = lvl()
    
    #max mob life
    mob_max_hp = int(mob_lvl) * int(mob_hp)
    #print(mob_max_hp)
    
    #min mob life
    mob_min_hp = mob_max_hp % 3
    #print(mob_min_hp)
    
    #random mob life from min to max
    mob_life_rand = random.randint(mob_min_hp, mob_max_hp)
    #print("mob random HP=" + str(mob_life_rand)) 
    return mob_life_rand


print("mob_hp " + str(random_mob_hp()))
#random_mob_hp()
