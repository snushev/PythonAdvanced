class ValueCannotBeNegative(Exception):
    pass


for n in range(5):
    if int(input()) < 0:
        raise ValueCannotBeNegative