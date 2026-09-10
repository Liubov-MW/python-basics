# WEEK 2 – IF / ELSE

# Aufgabe 1: Alter
age = 25

if age >= 18:
    print("Volljährig")
else:
    print("Minderjährig")


# Aufgabe 2: Positive, negative oder null
number = -5

if number > 0:
    print("Die Zahl ist positiv")
elif number < 0:
    print("Die Zahl ist negativ")
else:
    print("Die Zahl ist null")


# Aufgabe 3: Prüfung
score = 80

if score >= 90:
    print("Sehr gut")
elif score >= 75:
    print("Gut")
elif score >= 50:
    print("Bestanden")
else:
    print("Nicht bestanden")


# Aufgabe 4: Zutritt
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Zutritt erlaubt")
else:
    print("Zutritt verweigert")


# Aufgabe 5: Login
username = "Liubov"
password = "1234"

if username == "Liubov" and password == "1234":
    print("Login erfolgreich")
else:
    print("Login fehlgeschlagen")
