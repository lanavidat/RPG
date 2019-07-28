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
    from launcher import lets_go

    a = input("{: ^80}".format("Начнем изучение нового мира!"))
    #1from launcher import lets_go
    if not a:
        
        lets_go()
    else:
        lets_go()