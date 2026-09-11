n = int(input())
o = n % 10
h = n // 100
print("Success" if o + h < 10 else "Failure")
