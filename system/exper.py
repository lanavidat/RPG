import math

exp = 0



def exper():
    from system.random_mob_hp import mob_hp
    global exp
    exp = mob_hp()
    exp /=  25
    i = round(exp, 2)
    exper = open("system/hero/hero_char.py", "r")
    b = exper.readline()
    a = eval(b)
    a["exper"] += i
    exper.close()
    # запись полученного словаря(полночтью) в файл
    exper = open("system/hero/hero_char.py", "w")
    exper.write(str(a))
    exper.close()
    return i

def new_exp():
    return round(exp, 2)