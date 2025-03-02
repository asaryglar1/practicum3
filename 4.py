X, Y, N = map(int, input().split())
profit = (X*100+Y)*N
R = profit//100
K = profit-R*100
print(f'{R} руб. {K} коп.')
