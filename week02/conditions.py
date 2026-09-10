# WEEK 2 – IF / ELSE

# Example 1: Age
age = 25

if age >= 18:
    print("Volljährig")
else:
    print("Minderjährig")


# Example 2: Positive, negative or zero
number = -5

if number > 0:
    print("Die Zahl ist positiv")
elif number < 0:
    print("Die Zahl ist negativ")
else:
    print("Die Zahl ist null")


# Example 3: Score
score = 80

if score >= 90:
    print("Sehr gut")
elif score >= 75:
    print("Gut")
elif score >= 50:
    print("Bestanden")
else:
    print("Nicht bestanden")


# Example 4: Access
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Zutritt erlaubt")
else:
    print("Zutritt verweigert")


# Example 5: Login
username = "Liubov"
password = "1234"

if username == "Liubov" and password == "1234":
    print("Login erfolgreich")
else:
    print("Login fehlgeschlagen")
