# from system.hero.hero_info import gold
from system.random_mob_hp import mob_hp
# from system.definition import luck_check
import random


def all_loot_gold():
    pass


# генератор денег
def new_gold_from_loot():
    total_gold_from_mob_life = float(mob_hp())
    random_gold_chance = float(random.randint(0, total_gold_from_mob_life))

    random_gold = float(random_gold_chance) * 0.01

    return random_gold


# кошель
def wallet():
    pass
