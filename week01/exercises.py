# Übung 1: Benutzereingabe und Begrüßung (Введення даних та привітання)
benutzer_name = input("Wie heißt du? ")
print("Hallo, " + benutzer_name + "! Willkommen beim Python-Kurs.")

# Übung 2: Rechnen mit zwei Zahlen (Обчислення з двома числами)
zahl1 = 10
zahl2 = 5

summe = zahl1 + zahl2
differenz = zahl1 - zahl2
produkt = zahl1 * zahl2

print("Summe:", summe)
print("Differenz:", differenz)
print("Produkt:", produkt)

# Übung 3: Alter berechnen (Розрахунок року народження)
aktuelles_jahr = 2026
alter = int(input("Wie alt bist du? "))
geburtsjahr = aktuelles_jahr - alter

print("Du bist ungefähr im Jahr", geburtsjahr, "geboren.")
