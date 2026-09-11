a = int(input())
b = int(input())
ta = (a // 10) % 10
tb = (b // 10) % 10
big = a if ta > tb else b
print(abs(big % 10 - big // 100))
