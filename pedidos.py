from clientes import clientes
from produtos import produtos 

pedidos = [
    {"cliente": "Chris Bumbster", "produto": "Café Expresso", "preco": 5.00},
    {"cliente": "Julio Balestrin", "produto": "Cappuccino", "preco": 7.00}
]

def registrar_pedidos():
    if not clientes or not produtos:
        print("cadastre ao menos 1 cliente e 1 produto antes de fazer um pedido.\n")
        return
    
    print("clientes disponiveis:")
    for i, c in enumerate(clientes):
        print(f"{i} - {c['nome']}")
    id_cliente = int(input("escolha o número de cliente:"))

    print("produtos disponiveis")
    for i, p in enumerate(produtos):
        print(f"{i} - {p['nome']} (R$ {p['preco']:.2f})")
    id_produto = int(input("escolha o número de produto:"))

    pedido = {
        "cliente":clientes[id_cliente]["nome"],
        "produto":produtos[id_produto]["nome"],
        "valor":produtos[id_produto]["preco"]    
    }

    pedidos.append(pedido)
    print("pedido registrado com sucesso.\n")

def listar_pedidos():
    if not pedidos:
        print("nenhum pedido registrado.\n")
    else:
        print("pedidos")
        for p in pedidos:
            print(f"{p['cliente']} pediu {p['produto']} | R$ {p['valor']:.2f}")
        print()