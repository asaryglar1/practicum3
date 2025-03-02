N = int(input())
C = int(input())
a = int(input())
page = (a-1)//(C*N)+1
line = ((a-1)%(C*N))//N+1
num = ((a-1)%(C*N))%N+1
print(f'страница {page} столбец {line} строка {num}')