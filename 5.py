def draw_rabbit(n):
    rabbit = [
        "(\\___/) " * n,
        "(='.'=) " * n,
        '(")_(") ' * n,
    ]
    for line in rabbit:
        print(line)
rabbit = int(input())
draw_rabbit(rabbit)

