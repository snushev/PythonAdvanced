be = 6
b = 32

while be > 0 and b > 0:
            be -= 1  # Всеки пчелояд убива 7 пчели
            b -= 7  # Всяка пчела убива 1 пчелояд
            print(f" -> {max(be, 0)} vs {max(b, 0)}")