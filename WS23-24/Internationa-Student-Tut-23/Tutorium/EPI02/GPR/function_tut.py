
def sum_range(n:int, m:int)->int:
    
    if (n>m):
        # We would return wrong value if the bigger number is our start point
        return sum_range(m,n)
    val = 0
    for x in range(n,m):
        val += x
    return val

# print(sum_range(1, 5))  # 15 as expected
# print(sum_range(5, 1))  # 15 as expected
# print(sum_range(1, 1))  # 1 as expected
# print(sum_range(-4, 1))  # -9 : (-4) + (-3) + (-2) + (-1) + 0 + 1 ... correct 

def zero_loops(n):
    i = 0
    while (n != 0.0):
        i += 1
        n = n/2
        #print(n)  # just for debugging
    return i

# print(zero_loops(10))  # 1078
# print(zero_loops(0.1)) # 1072
# print(zero_loops(0.05)) # should be one less 1071

def chess_board(n, m):
    number = 0
    first_number = 0
    for i in range(0, n):
        for j in range(0, m):
            print(number,end=" ")
            if (number == 0): number = 1
            else: number = 0
        print()  # new row
        if (first_number == 0):
            number = 1
            first_number = 1
        else:
            number = 0
            first_number = 0

# chess_board(5, 8)  
# chess_board(8, 5)  
# chess_board(-3, 8) # Doesn't work, numbers have to be positive, EXPECTED

def catalanscheConst(n = 10):
    i = 0
    cat_const = 0
    while i < n:
        cat_const = cat_const + get_next(i)
        i += 1
    return cat_const


def get_next(i):
    numerator = pow(-1, i)
    denominator = pow(2*i+1, 2)
    return numerator/denominator

# print(catalanscheConst())

def show_catalanscheConst_changes(n, m, step=10):
    """
    Just show how much has the variable changed between the values.
    """
    for x in range(n, m, step):
        c1 = catalanscheConst(x)
        c2 = catalanscheConst(x + step)
        print(f"n = {x}: {c1}; n = {x+step}: {c2}\nDifferenz: {c2-c1}\n")

#show_catalanscheConst_changes(1,34,3)
