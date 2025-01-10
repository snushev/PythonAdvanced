n = int(input())
regular = set()
vip = set()

for _ in range(n):
    guest = input()
    if guest[0].isdigit():
        vip.add(guest)
    else:
        regular.add(guest)

while True:
    who_came = input()
    if who_came == 'END':
        break
    elif who_came in regular:
        regular.remove(who_came)
    elif who_came in vip:
        vip.remove(who_came)

not_came = len(regular) + len(vip)
print(not_came)
if vip:
    print(*sorted(vip), sep='\n')
if regular:
    print(*sorted(regular), sep='\n')