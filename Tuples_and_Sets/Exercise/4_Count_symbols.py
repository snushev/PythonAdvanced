text = input()

data = {}
for element in text:
    data[element] = text.count(element)

sorted_data = dict(sorted(data.items(), key=lambda item: item[0]))

for key, value in sorted_data.items():
    print(f"{key}: {value} time/s")