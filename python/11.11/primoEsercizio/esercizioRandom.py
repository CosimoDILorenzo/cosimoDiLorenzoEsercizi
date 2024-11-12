from random import randint

list = []

for num in range(0,5):
    list.append(randint(1,10))

with open("prova.csv","w") as file:
    file.write(str(list));

with open("prova.csv","r") as file:
    contenuto = file.readlines()
    for el in contenuto:
        el = el.strip()[1:-1]
        numero = el.replace(" ", "").split(",")
        numero = [int(num) for num in numero] 

    num1 = int(input("Inserisci il primo numero per indovinare un numero compreso tra 1 e 10: "))
    num2 = int(input("Inserisci il secondo numero per indovinare un numero compreso tra 1 e 10: "))

    if num1 in numero and num2 in numero:
        print("Hai indovinato")
    else:
        print("Ritenta")
        







