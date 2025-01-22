def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width
    def perimeter():
        return 2 * (length + width)

    string = f""
    string += f"Rectangle area: {area(length, width)}\n"
    string += f"Rectangle perimeter: {perimeter(length, width)}"

    return string

print(rectangle(2, 10))