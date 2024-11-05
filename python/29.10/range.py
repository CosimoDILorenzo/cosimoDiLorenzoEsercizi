numero = int(input("Inserire un numero:"));
is_primo = True;
numeriPrimi = [];

if numero > 1:
    for i in range(2, numero):  
        if numero % i == 0:  
            is_primo = False 
            break  
    if is_primo:  
        print("Il numero è primo")
        numeriPrimi.append(numero)

for i in range(numero,-1,-1):
     print(i) 

risposta = input("Vuoi ripetere l'operazione ? Rispondi si o no: ");


while risposta == "si":
    nuovoNumero = int(input("inserire un nuovo numero:"))
    for i in range(nuovoNumero,-1,-1):
        print(i) 
    risposta = input("Vuoi ripetere l'operazione ? Rispondi si o no: ");