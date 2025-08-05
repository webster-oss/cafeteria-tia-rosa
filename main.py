from clientes import cadastrar_cliente, listar_clientes
from produtos import cadastrar_produto, listar_produtos
from pedidos import registrar_pedidos, listar_pedidos

def menu():
    while True:
     print("====CAFETERIA DA MAMA====")
     print("1. Cadastrar Cliente")
     print("2. Listar Clientes")
     print("3. Cadastrar Produto")
     print("4. Listar Produtos")
     print("5. Registrar Pedido")
     print("6. Listar Pedidos")
     print("0. Sair")
     opcao = input("Escolha uma opção").strip()

     if opcao == "1":
         cadastrar_cliente()
     elif opcao == "2":
         listar_clientes()
     elif opcao == "3":
         cadastrar_produto()
     elif opcao == "4":
         listar_produtos()
     elif opcao == "5":
         registrar_pedidos()
     elif opcao == "6":
         listar_pedidos()
     elif opcao == "0":
         print("Saindo do sistema.")
         break
     else:
         print("Opção inválida.\n")

menu()