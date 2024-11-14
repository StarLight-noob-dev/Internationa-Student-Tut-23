import random as r

def handlung1():
    val_1 = int(input("Give the first number: "))
    val_2 = int(input("Give the second number: "))

    while val_2 != 0:
        h = val_1 % val_2
        val_1, val_2 = val_2, h
    print("The LCD is:", val_1)

def handlung2():
    rand_num = r.randint(-20, 20)
    print("The randum number is:", rand_num)
    while rand_num < 15:
        rand_num = rand_num**2
    print("The number is bigger than 2")

# This is how was called or refered to in the task
def russische_bauernmultiplikation(n, m):
    result = 0

    while n > 0:
        if n % 2 == 1:  # If n is even sum m
            result += m
        n = n // 2  # devided the number by 2
        m = m * 2   # duplicate the value of m
    return result
