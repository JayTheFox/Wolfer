import random
lseng = "qwertyuiopasdfghjklzxcvbnm"
lsrus = "йцукенгшщзхъфывапролджэячсмитьбю"
lsspe = "!№;%:?*(()_+=#$"
lsnum = "0123456789"
lsbit = "01"
lstab = "   "
lsspa = " "
password = "1234"
def brutforce(attemps, mi, ma, ls):
    while attemps != 0:
        randword = ""
        for i in range(random.randint(mi, ma)):
            random.seed()
            randword = random.choice(ls) + randword
        print(randword)
        if randword == password:
            print("Success... password is: " + randword)
            break
        attemps = attemps - 1
# example:
bruteforce(10000, 0, 4, lsnum)
# _________________________________
#                                  |
# You also can read file as a list!|
# _________________________________|


