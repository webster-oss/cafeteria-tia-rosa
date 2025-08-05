clientes = [
    {"nome": "Chris Bumbster", "email": "Chis.gigante@gmail.com"},
    {"nome": "Julio Balestrin", "email": "julio.ba@gmail.com"},
    {"nome": "Renato Cariane", "email": "renato.cariri@gmail.com"},
    {"nome": "Ronnye Coleman", "email": "ronnyezinho@gmail.com"},
    {"nome": "Monkey D. Luffy", "email": "luffy.rei.pirata@gmail.com"}
]

def cadastrar_cliente():
    nome = input("nome do cliente:")
    email = input("email:")
    cliente = {"nome": nome, "email": email}
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    if not clientes:
        print("nenhum cliente cadastrado.\n")
    else:
        print("lista de clientes:")
        for c in clientes:
            print(f"-{c['nome']} | email: {c['email']}")
        print()