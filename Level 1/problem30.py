n = int(input())
t = (n // 10) % 10
h = (n // 100) % 10
cond = (t + h == 10) and (t > 7 or h > 7)
print("Success" if cond else "Failure")
