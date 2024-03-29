# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe,
# Yellow - Ripe, Brown - Overripe)

fruit_name = input("Enter fruit name: ")
fruit_color = input("Fruit color from [Green, Yellow, Brown]: ")

if fruit_color.lower() == "green":
    print(f"{fruit_name} is unripe.")
elif  fruit_color.lower() == "yellow":
    print(f"{fruit_name} is ripe.")
elif fruit_color.lower() == "brown":
    print(f"Warning! {fruit_name} is overripe.")
