k = int(input())
start = 'A'

for x in range(k):
    for y in range(len(start)):
        if start[y] == 'A':
            start = start.replace('A', 'B')
        if start[y] == 'B':
            start = start.replace('B', 'BA')
    print(start)



