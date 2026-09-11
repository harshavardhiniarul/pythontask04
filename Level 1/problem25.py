n = int(input())
t = (n // 10) % 10
h = (n // 100) % 10
print(n - 5 * (t == h))
