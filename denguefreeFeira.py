# Autor: Leonardo Gama Teixeira
# Componente Curricular: 2024.1 EXA854 - MI - ALGORITMOS (TP03) 
# Concluido em: 15/04/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import csv
from tabulate import tabulate
from datetime import datetime
import usagedef

InvalidOp = True
while InvalidOp == True:
    menuOp = input('''\n  
        ----------Menu Inicial----------
                    
        1- Buscar informações do sistema
        2- Ler arquivo
        3- Adcionar informações
        4- Comparar dados
        5- Sair

Selecione uma opção: ''')

    match menuOp:
        case "1":
            print("Buscar informações do sistema")
        case "2":
            with open('denguedata.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                print(tabulate(reader, headers='firstrow', tablefmt='rounded_grid'))
        case "3":
            with open('denguedata.csv','a', newline='') as csvfile:
                write = csv.writer(csvfile, delimiter=',')
                write.writerow()
            
        case "4":
            print("Comparar dados")  
        case "5":
            print("\nFinalizando programa")
            exit()
        case _:
            print("\nSelecione uma opção válida!\n")