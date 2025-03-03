n = None
shuffle = None
order = None

with open('shuffle.in', 'r') as f:
    n = int(f.readline().strip())
    shuffle = list(map(int, f.readline().strip().split(" ")))
    order = list(map(int, f.readline().strip().split(" ")))

for _ in range(3):
    temp = [0]*n
    for index in range(n):
        temp[index] = order[shuffle[index]-1]
    order = temp  

with open('shuffle.out', 'w') as f:
    for i in order:
        f.write(f"{i}\n")