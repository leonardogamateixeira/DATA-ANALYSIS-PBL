# Autor: Leonardo Gama Teixeira
# Componente Curricular: 2024.1 EXA854 - MI - ALGORITMOS (TP03) 
# Concluido em: 15/04/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import csv

InvalidOp = True
while InvalidOp == True:
    menuOp = input('''\n1- Buscar informações do sistema
2- Ler arquivo
3- Adcionar informações ao arquivo
4- Sair

Selecione uma opção: ''')

    match menuOp:
        case "1":
            print("oi")
        case "2":
            with open('denguedata.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in reader:
                    print(' '.join(row))
        case "3":
            print("Escreva")
        case "4":
            print("\nFinalizando programa")
            exit()
        case _:
            print("\nSelecione uma opção válida!\n")