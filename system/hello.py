import os


def line():
    print( '{0:~^80}' .format("~"))

def hello():
    os.system('cls||clear')
    line()
    line()
    hello_world = " Добро пожаловать в Лабиринты. Опасность ждет тебя! Будь осторожен! "
    print( '{0: ^80}' .format(hello_world).upper())
    line()
    line()
    print("{: ^80}".format("Начнем изучение нового мира!\n"))
    from launcher import lets_go
    a = input()
    #1from launcher import lets_go
    if not a:
        
        lets_go()
    else:
        lets_go()