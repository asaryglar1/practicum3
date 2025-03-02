raw = input('Enter number: ')
try:
    num = int(raw)
    print(num)
except ValueError:
    print("Not a number entered")