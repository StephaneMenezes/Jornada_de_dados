idade = 30 
nome = "Alice"

# No Python diferente de outra linguagens de programação, não necessita de tipagem. Ou seja, não necessita definir o tipo de uma variavel. 
print(type(idade))
print(type(nome))

#Utilizando o type hint

idade: int = 30
nome: str = "Alice"
altura: float = 1.75
estudante: bool = True
print(type(idade))
print(type(nome))
print(type(altura))
print(type(estudante))


idade: int = int(input("Digite sua idade: "))
print(type(idade))  # A saída será <class 'str'>, pois o input é uma string

# Usando type hint com listas:

produtos_01: list = ["Arroz", "Feijão", "Macarrão"]
produtos_02: list[str] = ["Arroz", "Feijão", "Macarrão"]
print(type(produtos_01))
print(type(produtos_02))


#Produtos dict

produto_01 = {
    "nome": "Sapato",
    "preco": 150.0,
    "quantidade": 2,
    "disponivel": True
}

produto_02 = {
    "nome": "Meias",
    "preco": 15.0,
    "quantidade": 5,
    "disponivel": True
}

produto_escolhido = int(input("Digite o numero do produto: "))
quantidade = int(input("Digite a quantidade de produtos desejados: "))
print(produto_escolhido)

if produto_escolhido == 1:
    if produto_01["disponivel"] == True:
        print(f"Produto escolhido: {produto_01['nome']}, Preço: {produto_01['preco']}")
        if quantidade < produto_01["quantidade"]:
            produto_01["quantidade"] -= quantidade
        elif quantidade == produto_01["quantidade"]:
            produto_01["quantidade"] = 0
            produto_01["disponivel"] = False
        elif quantidade > produto_01["quantidade"]:
            print("Quantidade solicitada maior que a disponível")
    else: 
        print("Produto indisponível")

elif produto_escolhido == 2:
    if produto_02["disponivel"] == True:
        print(f"Produto escolhido: {produto_02['nome']}, Preço: {produto_02['preco']}")
        if quantidade < produto_02["quantidade"]:
            produto_02["quantidade"] -= quantidade
        elif quantidade == produto_02["quantidade"]:
            produto_02["quantidade"] = 0
            produto_02["disponivel"] = False
        elif quantidade > produto_02["quantidade"]:
            print("Quantidade solicitada maior que a disponível")
    else: 
        print("Produto indisponível")

print(produto_01)
print(produto_02)


# type hint com dicionarios:

produto_01: dict[str, int | str | float | bool] = {
    "nome": "Sapato",
    "preco": 150.0,
    "quantidade": 2,
    "disponivel": True
}

print(type(produto_01["nome"]))
