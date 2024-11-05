def palindroma(string):
    parola_senza_spazi = string.replace(" ","").lower()
    return parola_senza_spazi == parola_senza_spazi[::-1];

print(palindroma(input("Digita una frase: ")))