text = input()

data = {}
for element in text:
    data[element] = text.count(element)


for key, value in sorted(data.items()):
    print(f"{key}: {value} time/s")

