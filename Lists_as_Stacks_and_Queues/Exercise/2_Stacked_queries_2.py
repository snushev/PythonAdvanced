n = int(input())
queries = []
reverse_queries = []

functions = {
    "1": lambda x: queries.append(int(x)),
    "2": lambda: queries.pop() if queries else None,
    "3": lambda: print(max(queries)) if queries else None,
    "4": lambda: print(min(queries)) if queries else None
}

for i in range(n):
    command = input().split()
    functions[command[0]](*command[1:])

print(*reversed(queries), sep=', ')