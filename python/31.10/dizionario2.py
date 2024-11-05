dizionario_scolastico = {};
contatore = 0;


for a in range(2):
    nome_studente = input("Inserire nome dello studente: ");

    voti_studente = [];

    for v in range(3):
        voto = input("inserire voto dello studente " + nome_studente + ": ");
        voti_studente.append(voto)

    dizionario_scolastico["nome"] = nome_studente;
    dizionario_scolastico["voti"] = voti_studente;

print(dizionario_scolastico)




