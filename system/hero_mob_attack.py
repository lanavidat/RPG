#attack
import random
import os 
import time
from system.hero_hit import hero_hit, max_hero_hit
#from system.exper import new_exp, exper
from system.hero.hero_quantity_mob import hero_quantity_mob
from system.hero.hero_quantity_died import hero_quantity_died
#from system.hero.hero_info import life, hero_name
from system.hero.mob_name import mob_name, mob_rand_name
from system.random_mob_hp import random_mob_hp, mob_hp
from system.mob_hit import mob_hit, max_mob_hit
from system.hello import line
from system.lets_go import hero_search, lets_go
from system.hero_next_lvl import hero_next_lvl
from system.hero.hero_info import agility, strenght, life, lvl, next_lvl, hero_name, exper



# Проверка на удачу в бою
def luck_now():
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
#шапка
def mob_info():
    h = hero_name()  
   
    line()
    do = " " + str(h) + " решил прорядить популяцию монстров "
    char = " Hit: < {}hp, ag: {} str: {}, life: {}НР, lvl: {}, exp: {}/{} " .format(max_hero_hit(), agility(), strenght(), life(), lvl(), exper(), next_lvl())


    print( '{0:~^80}' .format(do.upper()))
    print('{:~^80}'.format(char.upper()))
    

    # инфо про моба
    name_mob = " Враг: {}. life: {}hp. hit: < {}hp ".format(mob_name(), mob_hp(), max_mob_hit())
    print("{:~^80}".format(name_mob.upper(), end=" "))
    line()
    print()
    print("Идет бой. Чтобы не искать новых мобов после текущего боя нажми эникей\n")

def hero_mob_attack():


    mob_rand_name()
    random_mob_hp()



    if True:

        def combat():
            h = hero_name()
            max_hit = max_hero_hit()
            mob_life_attack = float(mob_hp())
            hero_life = float(life())
            
            mob_hit()
            max_mob_hit()
            m_ht = round(mob_hit(), 2)
            m_max_ht = round(max_mob_hit(), 2)
            sw = 0
            
    # начало боя
            while True:
                
    # отображает номер строки раунда     
                time.sleep(1)       
                sw += 1

                
    # кидаем костяшки на инициативу хода между мобом и гг
                hero_hits = round(hero_hit(), 2)
                mob_hits = round(mob_hit(), 2)
                hero_random = random.random()
                mob_random = random.random()
                
    # проверка на инициативу героя
                if hero_random >= mob_random:
                    os.system('cls||clear')
                    mob_info()
                    luck_now()
                    luck_check = luck_now()

    # проверка на удачу в бою
                    if luck_check == True:

    # если удача улыбнулась удар max + random_hit
                        max_hit = max_hero_hit()
                        hero_hits = max_hit + hero_hits
                        hero_hits = round(hero_hits, 2)
                        mob_life_attack -= hero_hits
                        int_mob_life = round(mob_life_attack, 2)
                        print(str(sw) + " Тебе улыбнулись сами боги! " + str(h) + " лупит со всей силы, на " + str(hero_hits) + "НР. В " +str(mob_name()) + "a осталось " + str(int_mob_life) + "HP")
                        time.sleep(5)
    # обычный удар героя
                    else:
                        mob_life_attack -= hero_hits
                        int_mob_life = round(mob_life_attack, 2)
                        print(str(sw) +" " + str(h) + " бъет на " + str(hero_hits) + "НР. В " +str(mob_name()) + "a осталось " + str(int_mob_life) + "HP")

    # проверка на смерть моба и выдача плюшек
                    if int_mob_life <= 0:
                        from system.exper import new_exp, exper
                        
                        line()
                        new_exp()
                        i = "\n" + str(h) + " победил "
                        print(str(i.upper()) + "{0}A.".format(mob_name().upper(), mob_name()))
                        print("Получено: Опыт - {} ед.\n".format(float(exper())))



    # зачисление еденичку за убийство
                        hero_quantity_mob()

    #проверка уровня
                        
                        hero_next_lvl()


    # запрос на новый бой

                        import signal
                          
                                
                        def timeout_handler(signum, frame):
                            raise TimeoutError()
                          
                          
                        signal.signal(signal.SIGALRM, timeout_handler)
                          
                          
                        def input_timer(note, timeout):
                            signal.alarm(timeout)
                            try:
                                s = input("")
                            except TimeoutError:
                                hero_search()
                                #return "Timeout"
                            finally:

                                signal.alarm(0)
                                #lets_go()
                            return s
                        #input_timer() 
                        print("Ищем нового противника... Для остановки нажми эникей")
                        input_timer(" ", 5)
                        lets_go()
                       # i = input("Продолжаем геноцид? (Поиск моба - Enter. Главное меню - 9): ")
                                                
                        #if i == "9":
                         #   lets_go()
                         
                        #else:
                         #   hero_search()
                         
    #  проверка на инициативу моба
                if hero_random <= mob_random:
                    os.system('cls||clear')
                    mob_info()
                   
    # удар моба
                    hero_life -= m_ht
                    int_hero_life = round(hero_life, 2)

    # сообщение про удар моба
                    print(str(sw) + " "+ str(mob_name()) + " кусает " + "героя"+ " на " + str(mob_hits) + "HP. Жизненых сил героя осталось всего " + str(int_hero_life) + "HP")
                    
    # проверка на смерть героя
                    if int_hero_life <= 0:
                        line()
                        print("\n     " + str(h.upper()) + " погиб не выдержав побоев.\n".upper())
                         
    # зачисление еденичку за убийство
                        hero_quantity_died()


                        import signal
                          
                                
                        def timeout_handler(signum, frame):
                            raise TimeoutError()
                          
                          
                        signal.signal(signal.SIGALRM, timeout_handler)
                          
                          
                        def input_timer(note, timeout):
                            signal.alarm(timeout)
                            try:
                                s = input("")
                            except TimeoutError:
                                hero_search()
                                #return "Timeout"
                            finally:

                                signal.alarm(0)
                                #lets_go()
                            return s
                        #input_timer() 
                        print("Ищем нового противника... Для остановки нажми эникей")
                        input_timer(" ", 2)

                        lets_go()
                        
                        #import time
                        #from threading import Thread


    # проверка на новую попытку напасть
                        #t = time.sleep(4)
                        #print(t -1)
                        #while True:
                         #   start = time.time()
#                            answer = int(input("Попытать счастье еще раз? (Поиск моба - Enter. Главное меню - 9): "))
#
 #                           if time.time() - start >= 1:
  #                              hero_search()
   #                             #hero_search()
    #                        else:
     #                           if i == 9:
      #                              lets_go()
       #                         else:
        #                            hero_search()
                                #time.sleep(3)
                                #hero_search()
                                #lets_go()
                         

        combat()