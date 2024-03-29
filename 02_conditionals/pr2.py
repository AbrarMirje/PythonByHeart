# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone
# gets a $2 discount on Wednesday.

age = int(input(("What's your age? ")))
day = input("Enter today's day: ").lower()
# adult_ticket_price = 12
# childrens_ticket_price = 8
# discount = 2

# First way:
# if age >= 18:
#     if day == 'wednesday':
#         print(f"{adult_ticket_price - discount}")
#     else:
#         print(adult_ticket_price)
# elif age <= 17:
#     if day == 'wednesday':
#         print(f"{childrens_ticket_price - discount}")
#     else:
#         print(childrens_ticket_price)


# Second way:
price = 12 if age >= 18 else 8

if day == 'wednesday':
    price -= 2

print(f"Ticket price for you ${price}")
