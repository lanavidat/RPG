#gamer CLI-RPG
print("---- Привет искатель приключений. Опасность ждет тебя! Будь осторожен! ----\n")




#Харакетеристика героя
agility = 1
strenght = 1
life = 10
luck = 1
exper = 0
lvl = 1
next_lvl = 10
quantity_mob = 0
gold = 0

def hero_quantity_mob():
	mobs = quantity_mob
	mobs_exp = mobs ++ 1
	print(mobs_exp)

#характеристики Героя по запросу
def hero_stat():
	print("Текущие характеристики: " + "\nЛовкость: " + str(agility) + "\nСила: " + str(strenght) + "\nУровень жизни: "+ str(life)+ "\nУровень героя: " + str(lvl) + "\nТекущий опыт: " + str(exper)+ "\nОпыт до следующего уровня: " + str(next_lvl) + "\nКоличество убитых монстров: " + str(hero_quantity_mob) + "\n" )
	lets_go()

#Характеристика моба
mob_agility = 1
mob_strenght = 1
mob_life = 2
mob_luck = 0
mob_exper = 0
mob_lvl = 1
mob_name = "Монстр"

#Система нападения на монста
def hero_mob_attak():
	print("\nТебе дорогу пересек " + str(mob_name) + " c " + str(mob_life) + " очками жизни")
	agr = input("Атаковать? y/n ")
	print("")
	mob_life_attak = mob_life
	if agr =="y":
		print("Ты напал на " + str(mob_name))
		while mob_life_attak >=0:
			print ("Очки жизни моснста: " + str(mob_life_attak))
			mob_life_attak -= strenght
		else:
			print(str(mob_name) + " погиб" + "\n")
			hero_quantity_mob()
			hero_search()
	else:
		print("Герой уклонился от боя\n")
		hero_search()

#Запуск сценария атаки
def hero_search():
	hero_search = input("Поискать нового монстра? y/n: ")
	if hero_search == "y":
		hero_mob_attak()
	else:
		print("Герой струсил\n")
		lets_go()

#Инициализация игры, вопрос "куда идем""
def lets_go():
	print("Что будешь делать?\nОхота на монстров: 1\nПросмотр своих статов: 2\nВыйти в консоль: ex:")
	else_lets_go = input("Твое решение: ")
	print("")
	lets_go_go = str(else_lets_go)
	if lets_go_go == "1":
		hero_search()
	elif lets_go_go == "ex":
		print("Выход")
	elif lets_go_go == "2":
		hero_stat()
	else:
		print("Герой в замешательстве вертит головой")
		lets_go()

#Запуск игры		
lets_go()