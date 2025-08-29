''' O que é uma variavel Global: 
É uma variavel que são definidas fora de qualquer função e podem ser acessadas em qualquer parte do programa:'''

print(10*"-", "PRIMEIRO EXEMPLO: ENTENDENDO VARIAVEIS GLOBAIS", 10*"-")

x = 10 #Variavel Global

def minha_funcao():
    x = 8 #Variavel local dentro da função
    print(x)

minha_funcao()
print(x) #Acessando a variavel global fora da função

print(10*"-", "SEGUNDO EXEMPLO: ALTERANDO VARIAVEIS GLOBAIS", 10*"-")
#Notamos pelo print que por mais que dentro da função, tenhamos alterado o valor de x, fora da função o valor de x
#permanece o mesmo! 

# Para alterar o valor de uma variavel global podemos usar a palavra chave global

def minha_funcao2():
    global x 
    x = 8 
    print(x)

minha_funcao2()
print(x)