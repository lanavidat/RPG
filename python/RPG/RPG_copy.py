#gamer CLI-RPG
print("Привет искатель приключений. Опасность ждет тебя! Будь осторожен!\n")

agility = 1
strenght = 1
life = 10
luck = 1
exper = 0
lvl = 1
next_lvl = 10

#def hero():
#	hero_agility = 1
#	hero_strenght = 1
#	hero_life = 10
#	hero_luck = 1
#	hero_exper = 0
#	hero_lvl = 1
#	hero_next_lvl = 10
print("Текущие характеристики: " + "\nЛовкость: " + str(agility) + "\nСила: " + str(strenght) + "\nУровень жизни: "+ str(life)+ "\nУровень героя: " + str(lvl) + "\nТекущий опыт: " + str(exper)+ "\nОпыт до следующего уровня: " + str(next_lvl) + "\n")


mob_agility = 1
mob_strenght = 1
mob_life = 2
mob_luck = 0
mob_exper = 0
mob_lvl = 1
mob_name = "Монстр"




def hero_mob_attak():
	agr = input("hit?")
	mob_life_attak = mob_life
	if agr =="y":
		while mob_life_attak >=0:
			print (mob_life_attak)
			mob_life_attak -= strenght
		else:
			hero_search()

	else:
		print("off")



#hit = strenght - mob_life

'''
def hero_mob_attak():
	hit = input("hit the Mob? y/n ")
	mob_life_hit = mob_life
	if hit == "y":
		#print("mob`s life: ") + str(mob_life()))
		mob_life_hit -= strenght
		print(mob_life)
		hero_mob_attak()
'''

'''
def hero_mob_attak():
	#while mob_life:

	mob_life_attak = mob_life
	print("Уровень жизни монстра: " + str(mob_life_attak) + "\n")
	a = input("Ударить его? y/n? ")
	if a == "y" and mob_life_attak > 0:
				#mob_attack()
		#hero_mob_attak()
		mob_life_attak -= strenght
		hero_mob_attak()
	elif a =="y" and mob_life_attak <= 0:
		print("Ты убил монстра")
		print("Твой опыт увеличился на " + str(mob_life) +"ед.")
	else:
		print("Герой убежал")
				#break;

'''


'''
def mob_attack():
	print("Монстр На горизонте! \n" + "У него жизней: " + str(mob_life))
	atk = input("Напасть?: ")
	#print(atk)
	if atk == "y":
		#if mob_life > 0:
		hero_mob_attak()

	else:
		print("Hero is goooo")
	'''

'''
def attack():
	print("Поискать нового монстра?")

	go_attack = bool(input())
	while attack == True:
		mob_attack()
'''

#attack()

def hero_search():
	hero_search = input("Поискать нового монстра? y/n: ")
	if hero_search == "y":
		hero_mob_attak()
	else:
		print("Герой струсил")
hero_search()
