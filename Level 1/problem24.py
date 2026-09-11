n = int(input())
o = n % 10
h = n // 100
print(n - 5 * (o == h))
