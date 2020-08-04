
"""
Modalità di lettura del file:
-r mode (legge)
-w mode (sovrascrive)
-a mode (aggiunge)
-x mode (crea)
"""

f = open("Documento.txt","w")
print(f.write("Questo testo sovrascriverà l'attuale"))

f = open("Documento.txt","r")
print(f.read())


f = open("Documento.txt","a")
print(f.write("\nQuesto testo verrà aggiunto all'attuale"))

f = open("Documento.txt","r")
print(f.read())

""" mettere l'intero percorso quando si vuole creare un file al di fuori della cartella attuale"""

f = open("/Users/maria/Desktop/python/test.txt","r")
