n = int(input())
queries = []
reverse_queries = []

for i in range(n):
    command = input().split()
    if command[0] == '1':
        queries.append(int(command[1]))
    elif queries:
        if command[0] == '2':
            if queries:
                queries.pop()
        elif command[0] == '3':
            max_num = max(queries)
            print(max_num)
        elif command[0] == '4':
            min_num = min(queries)
            print(min_num)


while queries:
    print(queries.pop(), end='')
    if queries:
        print(", ", end='')