produtos = [
    {"nome": "Café Expresso", "preco": 5.00},
    {"nome": "Cappuccino", "preco": 7.00},
    {"nome": "Chocolate Quente", "preco": 10.90},
    {"nome": "Misto Quente", "preco": 10.00},
    {"nome": "Pão de Queijo", "preco": 5.00}
]


def cadastrar_produto():
    nome = input("nomde do produto:")
    preco = float(input("preço (R$):"))
    produto = {"nome": nome, "preco": preco}
    produtos.append(produto)
    print("produto cadastrado com sucesso!.\n")

def listar_produtos():
    if not produtos:
        print("nenhum produto cadastrado.\n")
    else:
        print("cardápio")
        for p in produtos:
            print(f"-{p['nome']} | R$ {p['preco']:2f}")
        print()