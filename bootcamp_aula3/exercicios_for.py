# Exercicios for: 
#Escreva um programa em Python que use um for para imprimir todos os números pares de 0 a 20
# for i in range(0,20,2):
  #  print(i)

#Dada a lista numeros = [3, 7, 2, 8, 10], use um for para calcular a soma de todos os elementos e exibir o resultado.
numero = [3,7,2,8,10]
soma = 0 

for i in numero: 
    soma += i
    print(soma)



num = int(input("Digite um número para ver sua tabuada: "))

for i in range(1,11): 
    print(f"{num} x {i} = {num*i}")

