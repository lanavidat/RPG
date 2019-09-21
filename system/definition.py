import random




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
