# i)

# Initial list of favorite foods
favorite_foods = ['Pizza', 'Sushi', 'Chocolate', 'Pasta', 'Tacos']

# Add two more items to the list by appending
favorite_foods.append('Ice Cream')
favorite_foods.append('Burgers')

# Remove one item from the list
favorite_foods.remove('Chocolate')

# Print the updated list
print("Updated list of favorite foods:")
print(favorite_foods)



# ii)

# Given list of numbers
numbers = [2, 5, 8, 10, 3, 6]

# Print the first and last elements of the list
first_element = numbers[0]
last_element = numbers[-1]
print("First element:", first_element)
print("Last element:", last_element)

# Print the list in reverse order
reversed_numbers = numbers[::-1]
print("List in reverse order:", reversed_numbers)

# Calculate and print the sum of all the elements in the list
total_sum = sum(numbers)
print("Sum of all elements:", total_sum)
