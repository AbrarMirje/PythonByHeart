# Coynting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
for number in numbers:
    if number > 0:
        count += 1

print(f"There are {count} positive numbers.")
print(f"There are {len(numbers) - count} negative numbers.")
