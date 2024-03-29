import random
print(random.random()) # random number between 0 to 1(exclusive)

print(random.randint(1, 100)) # random number between 1 to 100(exclusive)


# It will print random number from l1 list
l1 = ['Car', 'Villa', 'Cricket-kit', 'Food']
print(random.choice(l1))


# We can shuffle the things 
random.shuffle(l1)
print(l1)


# Game of Decimal

print(0.1 + 0.1 + 0.1 - 0.3) # 5.551115123125783e-17
# In above line we got unexpected output

# We can make correct it by using below library
from decimal import Decimal
cal = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') # 0.3
print(cal)

# Now we can correct the above unexpected ouput
print(cal - Decimal('0.3')) # 0.0


# We can import fractions also
# from fractions import Fraction

