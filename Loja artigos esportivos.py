#Programa de loja de artigos esportivos

# Biblioteca datetime para trabalhar com datas e horas
from datetime import datetime

# Mensagem de boas-vindas
print (" ")
print("************************") 
print("****  BEM VINDO A  ****")
print("*******  LOJA  *******")
print("***  ESPORTE TOTAL  ***")
print("************************")
print(" ")

# Dicionário para armazenar informações sobre os produtos (nome, quantidade, valor)
inventario = { 
    "Bola": {"quantidade": 10, "valor": 5.0},
    "chuteira": {"quantidade": 8, "valor": 4.0},
    "camiseta": {"quantidade": 25, "valor": 8.0},
    "garrafa": {"quantidade": 2, "valor": 78.0},
    "mochila" : {"quantidade": 10, "valor": 5.0},
    "shorts" : {"quantidade": 10, "valor": 9.0},
    "raquete": {"quantidade": 10, "valor": 7.0}

}


# Calcula a quantidade total de produtos no inventário
soma_inventario = 0
for val in inventario.values():
    soma_inventario += val ["quantidade"]

# Solicita o nome e sobrenome do cliente
print (" ")
print("Por favor insira seu nome")
nome = input()
print (" ")
print("Por favor insira seu sobrenome")
sobrenome = input()

nome_completo = nome + " " + sobrenome # Concatena o nome e sobrenome

#Agradecimento
print (" ")
print("Obrigado por nos visitar,", nome_completo)

compras = [] # Lista para armazenar as compras realizadas

# Função para mostrar o menu de opções
def mostrar_menu():
    print ("")
    print ("=======================================")
    print (" ")
    print ("Selecione a opção que deseja")
    print ("1. Conhecer quais produtos a loja tem")
    print ("2. Comprar um produto")
    print ("3. Mostrar compras")
    print ("4. Sair do programa")

# Função para mostrar o inventário completo
def mostrar_inventário():
    print (" ")
    print ("***  INVENTÁRIO  ***/n")
    for chave, valor in inventario.items():
        print (f"    {chave}: {valor}")
    print (" ")
    print ("Em total temos",soma_inventario, "produtos")

# Função para realizar uma compra
def comprar_produto():
    # Cria uma lista para armazenar os produtos escolhidos pelo cliente
    carrinho = []

    # Loop para adicionar produtos ao carrinho
    while True:
        print (" ")
        print ("Qual produto deseja comprar? Só pode escolher um de cada produto")
        print ("Escreva F para terminar a lista. Ou V para consultar seu carrinho/n")
        produto = input()
        if produto == "F": break

        if produto == "V": 
            if carrinho:    
                print (" ")
                print (f"Seu carrinho de compras contém {carrinho}")
            else: 
                print (" ")
                print ("Seu carrinho está vazio")

            continue

        if produto not in inventario:
            print (" ")
            print (f"Sentimos muito, mas não temos {produto} em nossa loja.")
        elif inventario [produto] == 0:
            print (" ")
            print (f"Sentimos muito, não temos mais {produto} em nossa loja.")
        elif produto not in carrinho:
            carrinho.append(produto)
        else:
            print (" ")
            print ("Esse produto ja está em seu carrinho.")

    print(" ")
    print("O conteúdo do seu carrinho é:")
    # Calcula o valor total da compra
    valor_total = 0
    for produto in carrinho:
        print(f"      {produto}: R${inventario[produto]['valor']:.2f}")
        # Adiciona o valor do produto ao valor total
        valor_total += inventario[produto]['valor']
        # Atualiza a quantidade do produto no inventário
        if inventario[produto]["quantidade"] > 0:
            inventario[produto]["quantidade"] -= 1
        else:
            print(f"Atenção: {produto} está com estoque zerado.")

    # Exibe o valor total da compra
    print(f"Valor total da compra: R${valor_total:.2f}")

    # Armazena a compra no histórico
    data = datetime.now()
    compras.append((nome, carrinho, data, valor_total))

# Função para mostrar o histórico de compras
def mostrar_compras():
    print("")
    print("*****  COMPRAS REALIZADAS  ****")
    for compra in compras:  # compra é uma tupla com nome, carrinho, data, valor_total
        nome, carrinho, data, valor_total = compra
        print(f"    {nome} comprou {carrinho} em {data}. Valor total: R${valor_total:.2f}")

# Loop principal do programa
while True:
    # Mostra o menu e recebe a opção do usuário
    mostrar_menu()
    resposta = int(input ())

    if resposta == 1:
        mostrar_inventário()
    elif resposta == 2:
        comprar_produto()

    elif resposta == 3:
        mostrar_compras()
    elif resposta == 4:
        print (" ")
        print ("Obrigado por usar o programa :D")
        break
