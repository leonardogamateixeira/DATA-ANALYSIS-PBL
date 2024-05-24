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

try:
    csvfileW = open('denguedata.csv', 'a', newline='')
    csvfileR = open('denguedata.csv', 'r')
    reader = csv.reader(csvfileR, delimiter=',')
except:
    print(IOError)

Lista = [row for row in reader]
bairros = set([row[1] for row in Lista])
datas = set([row[0] for row in Lista])
csvfileR.close()

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
            InvalidLocale = True
            while InvalidLocale:
                bairro = input("bairro: ")
                validation = usagedef.ValiBairro(bairros, bairro)
                if validation:
                    InvalidLocale = False
                else:
                    print(f"Não é possivel registrar o bairro {bairro} pois não consta no sistema.")
            InvalidNum = True
            while InvalidNum:
                suspeitos = input(f"suspeitos em {bairro}: ")
                negativos = input(f"negativos em {bairro}: ")
                confirmados = input(f"confirmados em {bairro}: ")
                validation = usagedef.ValiNum(suspeitos, negativos, confirmados)
                if validation:
                    InvalidNum = False
                else:
                    print("Digite valores válidos!")
            LastDate = Lista[-1][0]
            NewDate = usagedef.DayAdd(LastDate)
            habitantes = [row[2] for row in Lista if row[1] == bairro].pop()
            write = csv.writer(csvfileW, delimiter=',')
            write.writerow([NewDate, bairro, habitantes, suspeitos, negativos, confirmados])
            Lista.append([NewDate, bairro, habitantes, suspeitos, negativos, confirmados])

        case "4":
            print("Comparar dados")  
        case "5":
            print("\nFinalizando programa")
        case _:
            print("\nSelecione uma opção válida!\n")

csvfileW.close()