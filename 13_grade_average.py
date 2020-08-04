
    
"Calcolo media scolastica basata su uno o più test"

name = input("inserisci il nome dello studente: ")
last_name = input("inserisci il cognome dello studente: ")

data_valid = False

while data_valid == False:

    freshman = input("Inserisci la matricola dello studente: ")

    try:
        freshman = int(freshman)
        break
    except:
        print("Invalid Input. Sono accettati solo numeri.")
        continue
    
        data_valid = True

while data_valid == False:

    grade1= input("Inserisci il voto del tuo primo test: ")

    try:
        grade1= float(grade1)
    except:
        print("Invalid input. Sono accettati solo numeri. I decimali devono essere separati con il punto.")
        continue

    
    if grade1 < 0 or grade1 > 10:
        print("Il tuo voto dovrebbe essere tra 0 e 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:

    grade2= input( "Inserisci il voto del tuo secondo test: ")

    try:
        grade2= float(grade2)
    except:
        print("Invalid input. Sono accettati solo numeri. I decimali devono essere separati con il punto.")
        continue
    
    if grade2 < 0 or grade2 > 10:
        print("Il tuo voto dovrebbe essere tra 0 e 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:

    total_classes = input( "Inserisci il numero totale delle classi: ")

    try:
        total_classes = int(total_classes)
    except:
        print("Invalid input. Sono accettati solo numeri.")
        continue
    
    if total_classes <= 0:
        print("Il numero degli alunni non può essere meno o uguale a zero")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:

    absences = input( "Inserisci il numero totale delle assenze: ")

    try:
        absences = int(absences)
    except:
        print("Invalid input. Sono accettati solo numeri.")
        continue
    
    if absences < 0 or absences > total_classes:
        print("Il numero delle assenze non può essere meno di 0 o non può essere più grande del numero totale delle classi")
        continue
    else:
        data_valid = True

avg_grade = (grade1+grade2)/2
attendance = (total_classes - absences)/ total_classes

"""print zone"""

print("Nome studente: ",name)
print("Cognome studennte: ",last_name)
print("Matricola studente: ",freshman)
print("Media del voto: ",round(avg_grade,2))
print("Tasso di partecipazione: ",round(attendance,2))


if (avg_grade >=6 and attendance >= 0.8):
    print("Lo studente è passato con successo")
elif (avg_grade <6 and attendance <0.8):
    print("Lo studente non è passato poichè la media dei voti è più bassa di 6.0 e la il suo tasso di partecipazisone è più basso del 80%.")
elif (attendance >= 0.8):
    print("Lo studente non è passato poichè la media dei voti è più bassa di 6.0.")
else:
    print("Lo studente non è passato poichè il suo tasso di partecipazisone è più basso del 80%.")
            
            
