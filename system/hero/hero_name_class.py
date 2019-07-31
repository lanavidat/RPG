


def hero_name():
    i = open("system/hero/about_hero.py", "r")
    b = i.readline()
    a = eval(b)
    c = a["hero_name"]
    return c

def hero_class():
    i = open("system/hero/about_hero.py", "r")
    b = i.readline()
    a = eval(b)
    c = a["hero_class"]
    return c

def change_hero_name():
    pass

def change_hero_class():
    pass