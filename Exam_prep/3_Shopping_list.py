def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    basket = 5
    result = []

    for item, price in kwargs.items():
        total_price = price[0] * price[1]
        if total_price < budget:
            budget -= total_price
            basket -= 1
            result.append(f"You bought {item} for {total_price:.2f} leva.")
            if basket == 0:
                return '\n'.join(result)
    return '\n'.join(result)

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
