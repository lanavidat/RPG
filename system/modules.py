# from system.modules import


module = open("system/list_of_modules.py", "r")
b = module.readline()
a = eval(b)
module_wallet_on = a["module_wallet"]
module_gold_on = a["module_gold"]
module_statistics_on = a['module_more_statistics']
module_loot_on = a['module_loot']
module_expended_statics_on = a['module_expended_statics']
module_test_on = a['module_test']
module_cheat_mode_on = a['cheat_mode']


# проверка на включение модуля денег
def module_cash_switch():
    if module_wallet_on == 1 and module_gold_on == 1:
        module_on = 1
        return module_on


# проверка на включенность модуля для доп.статистики
def module_statistics_switch():
    if module_statistics_on == 1:
        module_on = 1
        return module_on


# проверка на включенность модуля для доп.статистики
def module_loot_switch():
    if module_loot_on == 1:
        module_on = 1
        return module_on


# Проверка на включенность модуля дополнительной статистики во время боя
def module_expended_statics_switch():
    if module_expended_statics_on == 1:
        module_on = 1
        return module_on


# Проверка на включенность модуля TEST
def module_test_switch():
    if module_test_on == 1:
        module_on = 1
        return module_on


# Проверка на включенность модуля CHEAT
def module_cheat_mode_switch():
    if module_cheat_mode_on == 1:
        module_on = 1
        return module_on


module.close()


# ------------------------------------------------------------------#

# запуск модуль денег
def module_wallet():
    module_on = module_cash_switch()
    if module_on == 1:
        from system.definition import line
        from system.hero.hero_info import gold
        print("Кошель:{:<21}{}".format("", round(gold(), 2)))
        line()


# модуль отображение дополнительной статистики
def module_more_statistics():
    module_on = module_statistics_switch()
    if module_on == 1:
        from system.definition import line
        from system.hero.hero_info import agility, strenght, life, lvl, next_lvl, hero_name, hero_died, luck, \
            quantity_mob, gold, exper
        print("Всего боевых раундов:{: <27} construct".format(""))
        print("Количество побед/смертей героя:{: <15}{}/{}".format("", quantity_mob(), hero_died()))
        line()


# запуск модуля лута
def module_loot():
    module_on = module_loot_switch()
    if module_on == 1:
        print("Hero loot:{: <20} construct".format(""))


# запуск модуля доп.статистики во время боя
def module_expended_statics():
    i = module_expended_statics_switch()
    return i


# запуск модуля TEST
def module_test():
    module_on = module_test_switch()
    return module_on


# запуск модуля CHEAT
def module_cheat_mode_launcher():
    cheat = open("system/hero/hero_char.py", "r")
    t = cheat.readline()
    y = eval(t)
    y["agility"] = 100
    y['strenght'] = 100
    y['life'] = 100
    cheat.close()
    # запись полученного словаря(полноcтью) в файл
    cheat_mode = open("system/hero/hero_char.py", "w")
    cheat_mode.write(str(y))
    cheat_mode.close()

    module = open("system/list_of_modules.py", "r")
    b = module.readline()
    a = eval(b)
    a["cheat_mode"] = 1
    module.close()
    # запись полученного словаря(полноcтью) в файл
    module = open("system/list_of_modules.py", "w")
    module.write(str(a))
    module.close()

    print("Модуль 'cheat_mode' ON. Нужен перезапуск игры")


# Выключение чит режима
def module_cheat_mode_off():
    import shutil
    shutil.copy('system/hero/hero_char_replace.py', 'system/hero/hero_char.py')

    module = open("system/list_of_modules.py", "r")
    b = module.readline()
    a = eval(b)
    a["cheat_mode"] = 0
    module.close()
    # запись полученного словаря(полноcтью) в файл
    module = open("system/list_of_modules.py", "w")
    module.write(str(a))
    module.close()

    print("Модуль 'cheat_mode' off. Нужен перезапуск игры")
