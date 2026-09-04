#WEEK2 - IF/ELIF/ELSE/AND
#Exercises

#Aufgabe 1. Alter
age=25
if age>=18:
    print("Volljährig")
else:
    print("Minderjährig")

#Aufgabe 2. Positive, negative oder null
number=-5
if number>1:
    print("Positive Zahl")
elif number<-1:
    print("Negative Zahl")
else:
    print("Null")

#Aufgabe 3. Prüfung
score=75
if score>=90:
    print("Sehr gut")
elif score>=75:
    print("Gut")
elif score>=60:
    print("Befriedigen")
else:
    print("Nicht bestanden")

#Aufgabe 4. Zutritt
age=17
has_ticket=True
if age>=18 and has_ticket:
    print("Zutritt erlaubt")
else:
    print("Zutritt verweigert")

#Aufgabe 5. Login
username="Liubov"
password="Python123"
if username=="Liubov" and password=="Python123":
    print("Login erfolgreich")
else:
    print("Login fehlgeschlagen")