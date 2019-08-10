
# уровень героя
def mob_lvl():
    q_mob_read = open("system/mob/mob_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["mob_lvl"]
    return b
    q_mob_read.close()

# ловкость
def mob_agility():
    q_mob_read = open("system/mob/mob_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["mob_agility"]
    return b
    q_mob_read.close()
# Сила
def mob_strenght():
    q_mob_read = open("system/mob/mob_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["mob_strenght"]
    return b
    q_mob_read.close()
# Life
def mob_life():
    q_mob_read = open("system/mob/mob_char.py", "r")
    b = q_mob_read.readline()
    #print(type(b))
    a = eval(b)
    b = a["mob_life"]
    return b

    q_mob_read.close()

# Gold
def mob_gold():
    q_mob_read = open("system/mob/mob_char.py", "r")
    b = q_mob_read.readline()
    #print(type(b))
    a = eval(b)
    b = a["mob_gold"]
    return b
    q_mob_read.close()

