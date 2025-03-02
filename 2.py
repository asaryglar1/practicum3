sec = int(input())
h = sec//60**2
m = sec//60-h*60
s = sec - m*60 - h*60**2
print(f'{h} часов {m} минут {s} секунд')