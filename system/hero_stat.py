import os


def hero_stat():
    os.system('cls||clear')
    do = " Характеристики игрока "

    print('{0:~^80}'.format("~"))
    print('{0:~^80}'.format(do.upper()))

    from system.definition import hero_statistics
    hero_statistics()

    a = input("\nИдем дальше...")
    if a or not a:
        from launcher import lets_go
        lets_go()
    else:
        hero_stat()
