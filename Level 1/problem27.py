n = int(input())
s = n // 100 + (n // 10) % 10 + n % 10
print("Success" if s == 10 else "Failure")
