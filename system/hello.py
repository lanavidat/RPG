import os


def line():
    print( '{0:~^80}' .format("~"))

def hello():
    os.system('cls||clear')
    print("\n\n\n")
    line()
    line()
    do = " Добро пожаловать в Лабиринты. Опасность ждет тебя! Будь осторожен! "
    print( '{0:~^80}' .format(do).upper())
    line()
    line()
    #print
    

    a = input("{: ^80}".format("Начнем изучение нового мира!"))
    #1from launcher import lets_go
    if a or not a:
        from launcher import lets_go
        lets_go()
