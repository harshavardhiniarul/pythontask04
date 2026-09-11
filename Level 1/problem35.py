a = int(input())
b = int(input())
sa = a % 10 + a // 100
sb = b % 10 + b // 100
big = a if sa > sb else b
print(big // 100 + (big // 10) % 10 + big % 10)
