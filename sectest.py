import csv
from tabulate import tabulate
from datetime import datetime
import usagedef
# Abre o arquivo e armazena em variaveis duas funções, uma para ler o arquivo e outra adicionar para adicionar uma linha ao final dele
try:
    csvfileW = open('denguedata.csv', 'a', newline='')
    csvfileR = open('denguedata.csv', 'r')
    reader = csv.reader(csvfileR, delimiter=',')
except FileNotFoundError:
    print("N existe, pergunta se quer criar um arquivo, cria e checa se ele tem ")
    
# Cria uma matriz baseada no arquivo aberto
# ADCIONAR VERIFICAÇÃO DE ARQUIVO<-isso com ctz //// talvez isso->CASO N TENHA FZR UM NOVO!
Lista = [row for row in reader]
datas = set([row[0] for row in Lista])

try:
    csvfileR.close()
except:
    print(IOError)