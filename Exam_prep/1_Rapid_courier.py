from collections import deque

packages_groups = [int(x) for x in input().split()]
courier_groups = deque([int(x) for x in input().split()])

total_weight = 0

while packages_groups and courier_groups:
    package = packages_groups.pop()
    courier = courier_groups.popleft()
    if courier >= package:
        courier -= package * 2
        if courier > 0:
            courier_groups.append(courier)
        total_weight += package
    elif courier < package:
        package -= courier
        packages_groups.append(package)
        total_weight += courier

print(f"Total weight: {total_weight} kg")

if not packages_groups and not courier_groups:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
if packages_groups:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages_groups))}")
if courier_groups:
    print(f"Couriers are still on duty: {', '.join(map(str, courier_groups))} but there are no more packages to deliver.")