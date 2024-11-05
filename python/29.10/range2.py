isPrimo = True;
numeriPrimi= [];
numeriNonPrimi = [];

ripeti = True;

while ripeti:
    numero1 = int(input("Inserisci il primo numero: "));
    numero2 = int(input("Inserisci il secondo numero: "));

    numeriPrimi.clear()
    numeriNonPrimi.clear()

    for num in range(numero1, numero2 + 1):
        if num > 1:
            is_primo = True 
            for i in range(2, num):
                if num % i == 0:
                    is_primo = False
                    break 
            if is_primo:
                numeriPrimi.append(num)
            else:
                numeriNonPrimi.append(num)

    print(f"Numeri primi nell'intervallo sono: {numeriPrimi}")
    print(f"Numeri non primi nell'intervallo sono: {numeriNonPrimi}")

    ripeti = input("Vuoi ripetere ? si/no: ").lower();

    if ripeti != "si":
        break;