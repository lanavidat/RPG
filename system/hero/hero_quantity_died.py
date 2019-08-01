def hero_quantity_died():
    # чтение количества уже убитых мобов их файла
   #чтение, сохраниене как словарь и +1 к словарю
    q_mob_read = open("system/hero/hero_char.py", "r")
    b = q_mob_read.readline()
    a = eval(b)
    a["hero_died"] += 1
    q_mob_read.close()
    # запись полученного словаря(полночтью) в файл
    q_mob_write = open("system/hero/hero_char.py", "w")
    q_mob_write.write(str(a))
    q_mob_write.close()
