import time


def thought(mine):
    def letter():
        time.sleep(5)
        print("Naan solla porathu onum unaku puthu ela")
        wait_time = 6
        time.sleep(wait_time)
        print("Irunthalum solluven")
        time.sleep(4)
        mine()
        time.sleep(1)
        print("This is what i wanna say You my dear chella pondatiiiiii")
    return letter()


def abino():
    print("I Love Sheryl Priscilla")


thought(abino)
