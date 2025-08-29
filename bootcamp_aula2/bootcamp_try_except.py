
#Analisando um erro especifico
try : 
    resultado = len(1)
    print(resultado)
except TypeError:
    print("Erro: Tipo de dado inválido.")



#Pedindo para retornar o erro
try: 
   resultado = len(4)
   print(resultado)
except TypeError as e:
    print(e) 

# Tentando ler um arquivo que não existe: 

import pandas as pd

try:
    read_csv = pd.read_csv("arquivo.csv")

except FileNotFoundError as e:
    print(e)
