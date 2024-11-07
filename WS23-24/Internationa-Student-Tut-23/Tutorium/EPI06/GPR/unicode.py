import random

def generate_arithmetic_puzzle(a, b):

    # Unicode Symbols defined
    symbols = [' ⨂ ', ' ⊟ ', ' ֍ ', ' ⊚ ', ' ∆ ', ' ∇ ', ' ⊘ ', ' ⨁ ', ' ⊛ ', ' ⊠ ']

    # add the numbers
    c = a + b

    # get Unicode version for each number
    a_sym = ''.join([symbols[int(digit)] for digit in str(a)])
    b_sym = ''.join([symbols[int(digit)] for digit in str(b)])
    c_sym = ''.join([symbols[int(digit)] for digit in str(c)])

    # put the string together
    transformed = f"{a_sym} + {b_sym} = {c_sym}"
    original = f"{a} + {b} = {c}"
    return original, transformed

# Beispielaufrufe
number1 = random.randint(1, 99)
number2 = random.randint(1, 99)

original, transformed = generate_arithmetic_puzzle(number1, number2)
print(f"The operation {original} when transformed looks: {transformed}")