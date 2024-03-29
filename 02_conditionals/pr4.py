# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars
# (Medium), >10 chars (Strong).

password = input("Enter password: ")
length = len(password) 

if length < 6:
    print("Password is Weak")
elif 6 <= length <= 10:
    print("Password is Medium")
else:
    print("Password is Strong")