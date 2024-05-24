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

# Abre o arquivo e armazena em variaveis duas funções, uma para ler o arquivo e outra adicionar para adicionar uma linha ao final dele
try:
    csvfileW = open('denguedata.csv', 'a', newline='')
    csvfileR = open('denguedata.csv', 'r')
    reader = csv.reader(csvfileR, delimiter=',')
except:
    print(IOError)
# Cria uma matriz baseada no arquivo aberto, uma lista todos os bairros cadastrados
Lista = [row for row in reader]
bairros = set([row[1] for row in Lista])
try:
    csvfileR.close()
except:
    print(IOError)

menuOp = ''
while menuOp != "5":
    menuOp = input("\n  ----------Menu Inicial----------\n1- Buscar informações do sistema\n2- Ler arquivo\n3- Adcionar informações\n4- Comparar dados\n5- Sair\nSelecione uma opção: ")

    match menuOp:
        case "1":
            InvalidFilt = True
            while InvalidFilt == True:
                filtro = input("\n1- Data\n2- Bairro\nPor qual parâmetro deseja buscar as informações?: ")
                match filtro:
                    case "1":
                        InvalidPam = True
                        while InvalidPam:
                            filtro = input("Digite a data desejada(dd/mm/YYYY): ")
                            datas = set([row[0] for row in Lista])
                            validation = usagedef.ValiDate(filtro, datas)
                            if validation == True:
                                rowFilt = 0
                                InvalidPam = False
                            else:
                                print(f"Não há registros para essa data.")
                    case "2":
                        InvalidPam = True
                        while InvalidPam:
                            filtro = input("Digite o bairro desejado: ")
                            validation = usagedef.ValiBairro(bairros, filtro)
                            if validation == True:
                                rowFilt = 1
                                InvalidPam = False
                            else:
                                print(f"Não há registros para o bairro {filtro}")
                    case _:
                        print("Digite uma opção valida!")

                TableFilt = [row for row in Lista if row[rowFilt] == filtro]
                print(tabulate(TableFilt, headers='firstrow', tablefmt='rounded_grid')) 
                InvalidFilt = False     
                        
        case "2": 
            print(tabulate(Lista, headers='firstrow', tablefmt='rounded_grid'))        
        case "3":
            LastDate = Lista[-1][0]
            InvalidOp = True
            while InvalidOp:
                NumOp = input("Deseja adcionar as informações no dia atual ou no próximo?\n1-Dia Atual\n2-Ir para o proximo dia\n")
                match NumOp:
                    case "1":
                        NewDate = LastDate
                        InvalidOp = False
                    case "2":
                        NewDate = usagedef.DayAdd(LastDate)
                        InvalidOp = False
                    case _:
                        print("\n Digite uma opção valida!")


            InvalidLocale = True
            while InvalidLocale:
                bairro = input("Qual bairro serão adcionadas as informações: ")
                validation = usagedef.ValiBairro(bairros, bairro)
                if validation:
                    habitantes = [row[2] for row in Lista if row[1] == bairro].pop()
                    InvalidLocale = False
                else:
                    print(f"\nNão é possivel registrar o bairro {bairro} pois não consta no sistema.\n")
                    Newbairro = input("Deseja adcionar um novo bairro ao sistema?\n1-Sim\n2-Não")
                    if Newbairro == "1":
                        bairro = input("Qual novo bairro que serão adcionadas as informações: ")
                    elif Newbairro == "2":
                        InvalidLocale = True
                    else:
                        print("Digite uma opção válida!")
            InvalidNum = True
            while InvalidNum:
                suspeitos = input(f"Quantidade de casos suspeitos em {bairro}: ")
                negativos = input(f"Quantidade de casos negativos em {bairro}: ")
                confirmados = input(f"Quantidade de casos confirmados em {bairro}: ")
                validation = usagedef.ValiNum(suspeitos, negativos, confirmados)
                if validation:
                    if (int(suspeitos) + int(negativos) + int(confirmados)) < int(habitantes):
                        InvalidNum = False
                    else:
                        print("O número de casos precisa ser menor que o número de habitantes!")
                else:
                    print("Digite valores válidos!")

            write = csv.writer(csvfileW, delimiter=',')
            write.writerow([NewDate, bairro, habitantes, suspeitos, negativos, confirmados])
            Lista.append([NewDate, bairro, habitantes, suspeitos, negativos, confirmados])

        case "4":
            print("Comparar dados")  
        case "5":
            print("\nFinalizando programa")
        case _:
            print("\nSelecione uma opção válida!\n")

try:
    csvfileW.close()
except:
    print(IOError)