# from system.modules import


module = open("system/list_of_modules.py", "r")
b = module.readline()
a = eval(b)
module_wallet_on = a["module_wallet"]
module_gold_on = a["module_gold"]
module_statistics_on = a['module_more_statistics']
module_loot_on = a['module_loot']

# проверка на включение моделя денег
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

module.close()

# запуск модуль денег
def module_wallet():
    module_on = module_cash_switch()
    if module_on == 1:
        from system.definition import line
        from system.hero.hero_info import gold
        print ( "Кошель:{:<21}{}".format("", round(gold(),2)))
        line()
    else:
        None

# модуль отображение дополнительной статистики
def module_more_statistics():
    module_on = module_statistics_switch()
    if module_on == 1:
        from system.definition import line
        from system.hero.hero_info import agility, strenght, life, lvl, next_lvl, hero_name, hero_died, luck, quantity_mob, gold, exper
        print ("Всего боевых раундов:{: <27} construct".format(""))
        print ("Количество побед/смертей героя:{: <15}{}/{}".format("", quantity_mob(), hero_died()))
        line()

# запуск модуля лута
def module_loot():
    module_on = module_loot_switch()
    if module_on == 1:
        print ("Hero loot:{: <20} construct".format(""))
