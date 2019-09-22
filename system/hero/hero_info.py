# к-во убитых мобов
def quantity_mob():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["quantity_mob"]
    return b
    q_mob_read.close()

# уровень героя
def lvl():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["lvl"]
    return b
    q_mob_read.close()

# Опыта до следующего уровня для героя
def next_lvl():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["next_lvl"]
    return b
    q_mob_read.close()

# ловкость
def agility():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["agility"]
    return b
    q_mob_read.close()

# Сила
def strenght():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["strenght"]
    return b
    q_mob_read.close()

# уровень жизни героя
def life():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["life"]
    return b
    q_mob_read.close()

# удача героя
def luck():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["luck"]
    return b
    q_mob_read.close()

# текущий опыт
def exper():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b =a["exper"]
    return round(b, 2)
    q_mob_read.close()

# деньги 
def gold():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["gold"]
    return b
    q_mob_read.close()

# количество смертей гг
def hero_died():
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    b = a["hero_died"]
    return b
    q_mob_read.close()

# имя героя
def hero_name():
    i = open("system/hero/about_hero.py", "r")
    b = i.readline()
    a = eval(b)
    c = a["hero_name"]
    return c

# класс героя
def hero_class():
    i = open("system/hero/about_hero.py", "r")
    b = i.readline()
    a = eval(b)
    c = a["hero_class"]
    return c
