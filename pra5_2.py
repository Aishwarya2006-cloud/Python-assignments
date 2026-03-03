# Create a program to store the Prices of sold items on a particular day of a shop in a Tuple
# Perform the following operations:
# a) Print the total number of items sold
# b) Print the price of cheapest item sold
# c) Print the price of costliest item sold
# d) Print the price list in ascending order
# e) Print the number of costliest items sold on the day

prices = tuple(map(int, input("Enter item prices separated by space: ").split()))

print("Total items sold:", len(prices))

print("Cheapest item price:", min(prices))

print("Costliest item price:", max(prices))

print("Prices in ascending order:", tuple(sorted(prices)))

costliest = max(prices)
print("Number of costliest items sold:", prices.count(costliest))