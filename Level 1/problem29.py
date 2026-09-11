n = int(input())
t = (n // 10) % 10
h = (n // 100) % 10
print("Success" if t + h > 10 else "Failure")
