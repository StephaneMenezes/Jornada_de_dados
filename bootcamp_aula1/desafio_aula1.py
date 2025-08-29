# Solicite ao usuário que digite seu nome:

nome_user = input("Digite seu nome: ")

# Solicite ao usuário que digite o valor do seu salário: 

salario_user = float(input("Digite o valor do seu salário: R$ "))

# Solicite ao usuário que digite o valor do bônus recebido

bonus_user = float(input("Digite o valor do bônus recebido: R$ "))

valor_total = salario_user + bonus_user

# Imprima o cálculo do KPI: 
print( f"O cálculo do KPI é calculado como: Salário Mensal R$ {salario_user} + Bônus recebido R$ {bonus_user} = R$ {valor_total}")

print(f"Olá {nome_user}, o seu recebimento total será de R$ {valor_total:.2f} reais. Resumo: Salário Mensal R$ {salario_user} + Bônus recebido R$ {bonus_user}")

#Desafio_Aula 1

#Adicionando mais um comentário para fazer o commit