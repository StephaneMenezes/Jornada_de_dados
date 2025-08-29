print("Hello World")

#Exercicios da aula 2: 

# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário. 

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

soma = num1 + num2

print(f"A soma entre {num1} e {num2} é igual a {soma}. ")

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

num = int(input("Digite um número inteiro: "))

num_div_5 = num%5

print(f"O resto da divisão de {num} por 5 é igual a {num_div_5}.")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

result = num1 * num2 

print(f"O resultado da multiplicação entre {num1} e {num2} é igual a {result}.")


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite outro número inteiro: "))

num_divisao_inteira = num_1 // num_2

print(f"A divisão inteira de {num_1} por {num_2} é igual a {num_divisao_inteira}.")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num = int(input("Digite um número inteiro: "))

quadrado = num ** 2 

print(f"O quadrado de {num} é igual a {quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

num_float_1 = float(input("Digite um número flutuante: "))
num_float_2 = float(input("Digite outro número flutuante: "))

soma_float = num_float_1 + num_float_2

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.


num_float_2 = float(input("Digite outro número flutuante: "))

media_float = (num_float_1 + num_float_2) / 2 

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário)

base = float(input("Digite um número como base: "))
expoente = float(input("Digite um número como expoente: "))

potencia = base ** expoente

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"A temperatura em Fahrenheit é: {fahrenheit}")

