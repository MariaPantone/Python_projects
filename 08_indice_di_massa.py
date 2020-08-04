print("Questo programma calcola il tuo indice di massa")

weight = float ( input("Digita il tuo peso in Kg (ex. 70.5): ") )
height =  float ( input("Digita la tua altezza in metri (ex. 1.70): "))

bmi = weight / (height ** 2)

print("Il tuo BMI è :",round(bmi,2))

if(bmi <= 18.5):
    classification = "sottopeso"
elif (bmi > 18.5 and bmi <= 24.9):
    classification = "normale"
elif (bmi > 24.9 and bmi <= 29.9):
    classification = "sovrappeso"
else:
    classification = "Obesità"


print("la classifizione del tuo BMI è:",classification)
    

    
