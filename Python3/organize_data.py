# Use of lists to organize sales data

toppings = ("pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms")
prices = (2, 6, 1, 3, 2, 7, 2)
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")
# Mixing toping and prices
pizzas = list(zip(prices, toppings))
pizzas.sort()


cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
print(three_cheapest)

# Counting how many instances of $2 slices
num_two_dollar_slices = prices.count(2)

