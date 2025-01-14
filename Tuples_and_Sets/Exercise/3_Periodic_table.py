#n = int(input())
# table = set()
#
# for i in range(int(input())):
#     elements = input().split()
#     for element in elements:
#         table.add(element)

table = {el for _ in range(int(input())) for el in input().split()}

print(*table, sep='\n')
