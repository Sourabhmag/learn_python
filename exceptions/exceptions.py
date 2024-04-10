a = 10
b = 0

try:
    print(a/b)
except Exception as e:
    print(e)
finally:
    print("Excption Handling")