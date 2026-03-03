"""Develop a program that asks the user to enter a series of integers and store them ina Tuple

Develop a program that asks the user to enter a series of integers and store them in a Tuple. Perform the following: a) Print the total number of items in the Tuple.

b) Print the last item in the Tuple.

c) Print the Tuple elements in reverse order.

d) Print Yes if the Tuple contains an integer 5 and No otherwise

e) Remove the first and last items from the Tuple, sort the remaining items, and print the result."""


nums = tuple(map(int, input("Enter integers separated by space: ").split()))
print("Total number of items:", len(nums))
print("Last item:", nums[-1])
print("Tuple in reverse order:", nums[::-1])

if 5 in nums:
    print("Yes")
else:
    print("No")

if len(nums) > 2:
    new_tuple = tuple(sorted(nums[1:-1]))
    print("After removing first and last & sorting:", new_tuple)
else:
    print("Not enough elements to remove first and last.")