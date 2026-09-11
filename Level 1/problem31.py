n = int(input())
s = sum(int(d) for d in str(n))
while s >= 10:
    s = sum(int(d) for d in str(s))
print(s)
