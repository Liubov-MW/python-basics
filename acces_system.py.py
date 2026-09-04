#Variablen erstellen
age=17
has_ticket=False
is_emploee=True
has_id=False
is_banned=True
score=45
#Überprüfe das Alter
if age>=18:
    print("Volljährig")
else:
    print("Minderjährig")
#Testergebnis überprüfen
if score>=90:
    print("Sehr gut")
elif score>=75:
    print("Gut")
elif score>=50:
    print("Bestanden")
else:
    print("Nicht bestanden")
#Zugriff überprüfen
if(age>=18 and has_ticket) or is_emploee:
    print("Zugang erlaubt")
else:
    print("Zugang verweigert")
#ID überprüfen
if has_id and not is_banned:
    print("ID akzeptiert")
else:
    print("ID abgelent")
#Zusammenfasend
if age>=18 and (has_ticket or is_emploee) and has_id and not is_banned and score>=50:
    print("Zugang vollständig erlaubt")
else:
    print("Zugang vollständig verweigert")