import os

def about_game():
    os.system('cls||clear')
    print("\
    	\
    	\
    	\
    	\n\n\n\n\n\n\nText about Game\
    	\
    	\
    	\
    	")
    i = input()
    if not i:
        from launcher import lets_go
        lets_go()
    else:

        lets_go()