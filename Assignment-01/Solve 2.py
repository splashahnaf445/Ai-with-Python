# Problem 2: The Grocery Ledger (Dictionaries)
# Fatima runs a small grocery stall. She keeps a dictionary where the keys are item names and the
# values are their prices.
# Write code that:
# 1. Stores at least 5 items and their prices in a dictionary.
# 2. Prints the name and price of the most expensive item.
# 3. Prints the total cost if someone buys everything on the list once.
# prices = {
# "rice": 60,
# "milk": 45,
# "eggs": 12,
# "bread": 35,
# "oil": 150
# }

prices = {
    "rice": 60,
 "milk": 45,
 "eggs": 12,
 "bread": 35,
 "oil": 150
}
maximum = 0

for item in prices:
    if(prices[item]>maximum):
        maximum=prices[item]
        string=item

print(f'Most expensive item is {string} and price : {maximum}')

cost=0
for item in prices:
    cost+=prices[item]
print(f'Total cost : {cost}')



