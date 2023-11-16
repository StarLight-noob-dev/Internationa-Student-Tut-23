
# Remember to use the BRAKE-POINTS please

# ------------------------
print("------ loops a --------")
# ------------------------
for x in range(0,12,3):
    print(x)
else: print(42)

# ------------------------
print("------ loops b --------")
# ------------------------
i = 0
j = 1
while i < j:
    i += 0.1
    print(i, " : ",j)
    if j > 1.5: break
    j -= -.2
else: print("B")

# ------------------------
print("------ loops c --------")
# ------------------------

i = 0
j = 1
while i < j:
    i += 0.1
    print(i, " : ",j)
    if j > 1.5: continue
    j -= -.2
else: print("B")

# ------------------------
print("------ funct a --------")
# ------------------------

def f1(n, m=5):
    if (n == m): return True
    print("n")
    if (n < m): return False

y = f1(6)

print(y)

# ------------------------
print("------ funct b --------")
# ------------------------

def f2(n, m):
    if (n < m): return f2(m, n)
    return m

y = f2(17, 19)

print(y)

# ------------------------
print("------ funct c --------")
# ------------------------

def f3(n):
    return n+a

a = 4
y = f3(6)

print(y)