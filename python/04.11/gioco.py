users = {
    1: {"nome": "cosimo", "password": "ciao", "punteggio": 0},
    2: {"nome": "giacomo", "password": "miao", "punteggio": 0},
    3: {"nome": "paolo", "password": "rosso", "punteggio": 0},
    4: {"nome": "mirko", "password": "giallo", "punteggio": 0}
}

def login():
    nome_utente = input("Inserisci nome utente: ")
    pwd = input("Inserisci password: ")
    for id_utente, user in users.items():
        if user["nome"] == nome_utente and user["password"] == pwd:
            print(f"Login effettuato per l'utente {nome_utente}")
            return True
        
    print(f"Nome utente o password sbagliata")
    return False

login()
