# Processar itens de uma lista até encontrar um valor especifico:

itens = ["Maçã", "Banana", "Laranja", "Uva", "Melancia", "Kiwi", "Tangerina"]
i = 0

fruta_desejada = input("Digite o nome da fruta que deseja encontrar: ")


while i < len(itens):
    if itens[i] == fruta_desejada: 
        print(f"{fruta_desejada} encontrada!")
        break 
    
    print(f"Processando item: {itens[i]}")
    i += 1
    