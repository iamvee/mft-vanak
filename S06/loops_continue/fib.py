a, b = 1, 1

for i in range(10):
    a, b = b, a + b
    print(b)