# Estruturas de repetição

# Verifica as condições até retornar a que se enquadra. 

x = 2.5

if x < 0 : 
    print("X é menor que zero")

elif x == 0:
    print("X é igual a zero")

elif x == 1: 
    print("X é igual a um")

elif x == 2: 
    print("X é igual a dois")

else: 
    print("X é maior que dois")

# Exericios: 

# Garantir que todos os valores do estoque sejam positivos: 

estoque = 120

if estoque > 0 : 
    print("O valor do estoque está positivo")

else: 
    print( "O valor do estoque está negativo")


''' Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta' '''

temp = int(input("Digite aqui o a temperatura em ºC: "))

if temp < 0 : 
        print(f"Você informou {temp} ºC - Classificação: Muito Baixa!")
elif temp < 18 : 
    print(f"Você informou {temp} ºC - Classificação: Baixa")

elif temp >= 18 and temp <= 26 : 
    print(f"Você informou {temp} ºC - Classificação: Normal")

else:   
    print(f"Você informou {temp} ºC - Classificação: Alta")
    

#Analisando logs: 

log = {'timestamp': '2021-06-23 10:00:00','level':'Error','message':'Falha na conexão'}

if log['level'] == 'Error':
    print(log['message'])
else:
    print(log['timestamp'])


#Analisando Multiplos Logs: 

logs = [
    {'timestamp': '2021-06-23 10:00:00','level':'Error','message':'Falha na conexão'},
    {'timestamp': '2021-06-23 10:01:00','level':'Warning','message':'Uso elevado de memória'},
    {'timestamp': '2021-06-23 10:02:00','level':'Info','message':'Sistema iniciado com sucesso'}
]

for log in logs: 
    if log['level'] in ['Error', 'Info']:
        print(f"{log['timestamp']} - {log['message']}")


'''
Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições 
e imprima "Dados de usuário válidos" ou o erro específico encontrado.
'''

idade = 24
email = input("Digite seu email: ")

if not 18 <= idade <= 65:
    print("Idade fora do intervalo permitido.")

elif "@" not in email or "." not in email : 
    print(f"O Email: {email} é inválido, por favor, inserir um email válido.")

else: 
    print("Dados de usuários válidos, seja bem vindo!")