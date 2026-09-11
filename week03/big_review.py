# Variable erstellen

name = "Liubov"
age = 34
is_employee = True
has_id = True
is_banned = False
score = 82
employees = ["Anna", "Maria", "Liubov", "Olena"]
scores = [45, 72, 90, 33, 81, 50]

# Prüfe mit if / else

if age >=18:
    print("Volljährig")
else:
    print("Minderjährig")
  
# Mitarbeiterstatus

if is_employee == True:
    print("Mitarbeiter")
else:
    print("Kein Mitarbeiter")
  
# Zugangskontrolle

if age >=18 and has_id and not is_banned:
    print("Zutritt erlaubt")
else:
    print("Zutritt verweigert")
  
# Ergebnis prüfen

if score>=90:
    print("Sehr gut")
elif score>=75:
    print("Gut")
elif score>=50:
    print("Bestanden")
else:
    print("Nicht bestanden")
  
# Mitarbeiterliste

for employee in employees:
    print(employee)
  
# Testergebnisse

for score in scores:
    if score>=50:
        print(score)
      
# Gerade Zahlen

for i in range(2, 22, 2):
    print(i)
  
# while

count = 1
while count<=5:
    print(count)
    count=count+1
  
# break

for i in range(1, 11):
    if i == 7:
        break
    print(i)
  
# continue

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
  
# 🏆 BONUS — alles kombinieren

ages = [12, 17, 18, 25, 16, 30, 14, 21]
for age in ages:
    if age==25:
        print("besondere Prüfung")
    elif age>=18:
        print("Volljährig")
    else:
        print("Minderjährig")
