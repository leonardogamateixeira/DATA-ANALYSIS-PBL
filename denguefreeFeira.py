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

# Cria uma matriz baseada no arquivo aberto
Lista = [row for row in reader]
datas = set([row[0] for row in Lista])

try:
    csvfileR.close()
except:
    print(IOError)

menuOp = ''
while menuOp != "5":
    menuOp = input("\n  ----------Menu Inicial----------\n1- Buscar informações do sistema\n2- Ler arquivo\n3- Adcionar informações\n4- Comparar dados\n5- Sair\nSelecione uma opção: ")
    # Cria uma lista com informações unicas baseado em todos os bairros cadastrados
    bairros = set([row[1] for row in Lista])

    match menuOp:

        case "1":
            InvalidFilt = True
            while InvalidFilt:
                # Pergunta ao usuario se ele quer filtrar a busca por data ou por bairro
                filtro = input("\n1- Data\n2- Bairro\nPor qual parâmetro deseja buscar as informações?: ")
                match filtro:
                    case "1":
                        InvalidPam = True
                        while InvalidPam:
                            # o usuario digita a data no formato solicitado, e o programa checa se existe uma data registrada com esse valor
                            filtro = input("Digite a data desejada(dd/mm/YYYY): ")
                            if usagedef.ValiDate(filtro, datas):
                                rowFilt = 0
                                InvalidPam = False
                            else:
                                print(f"Não há registros para essa data.")

                    case "2":
                        InvalidPam = True
                        while InvalidPam:
                            # o usuario digita um bairro e o programa checa se esse bairro está cadastrado no arquivo
                            filtro = input("Digite o bairro desejado: ")
                            if usagedef.ValiBairro(filtro, bairros):
                                rowFilt = 1
                                InvalidPam = False
                            else:
                                print(f"Não há registros para o bairro {filtro}")

                    case _:
                        print("Digite uma opção valida!")

                # ao final do loop, o programa entrega uma tabela com os dados filtrados
                TableFilt = [row for row in Lista if row[rowFilt] == filtro]
                print(tabulate(TableFilt, headers=['Data','Bairro','Habitantes','Casos Suspeitos','Casos Negativos','Casos Confirmados'], tablefmt='rounded_grid')) 
                InvalidFilt = False     
                        
        case "2":
            InvalidOp = True
            while InvalidOp:
                TableOp = input("1- Ver tabela com todos os dados\n2- Percentual de todos os casos\n3- Percentual de casos por bairro")
                match TableOp:

                    case "1":
                        InvalidOp = False
                        print(tabulate(Lista, headers='firstrow', tablefmt='rounded_grid'))

                    case "2":
                        InvalidOp = False
                        print("Percentual de todos os casos")

                    case "3":
                        InvalidOp = False
                        print("Percentual de casos por bairro")

                    case _:
                        print("Digite um valor valido")

        case "3":
            # Pega a ultima data da lista e armazena em LastDate
            LastDate, InvalidOp = Lista[-1][0], True
            while InvalidOp:
                # A adição de datas é automatica no programa, deixando o usuario apenas escolher se quer 
                # adicionar as informações no dia atual ou no próximo dia
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
                # Pergunta em qual bairro será adcionada as informações e checa se o bairro esta cadastrado
                bairro = input("Qual bairro serão adcionadas as informações?: ")
                if usagedef.ValiBairro(bairro, bairros):
                    habitantes = [row[2] for row in Lista if row[1] == bairro].pop()
                    InvalidLocale = False
                else:
                    print(f"\nNão é possivel registrar o bairro {bairro} pois não consta no sistema.\n")
            InvalidNum = True
            while InvalidNum:
                # Pede a atualização dos dados do bairro no dia e checa se os valores digitados são validos
                suspeitos = input(f"Quantidade de novos casos suspeitos em {bairro}: ")
                negativos = input(f"Quantidade de novos casos negativos em {bairro}: ")
                confirmados = input(f"Quantidade de novos casos confirmados em {bairro}: ")
                validation = usagedef.ValiNum(suspeitos, negativos, confirmados)
                if validation:
                    suspeitos, negativos, confirmados = list(map(int, [suspeitos, negativos, confirmados]))
                    # após isso checa se a soma dos casos não é maior que a quantidade de 
                    # habitantes do bairro e se a quantidade de casos negativos e confirmados não
                    # é maior que a quantidade de suspeitos anterior, caso não seja adiciona os casos a conta
                    if (suspeitos + negativos + confirmados) < int(habitantes):

                        LastSuspeitos = int([row[3] for row in Lista if row[1] == bairro].pop())
                        if negativos + confirmados < LastSuspeitos:

                            NewSuspeitos = (LastSuspeitos + suspeitos) - (negativos + confirmados)
                            NewNegativos = int([row[4] for row in Lista if row[1] == bairro].pop()) + negativos
                            NewConfirmados = int([row[5] for row in Lista if row[1] == bairro].pop()) + confirmados
                            InvalidNum = False
                        else:  
                            print("A soma dos casos positivos e negativos precisa ser menor que o número de casos suspeitos!")                 
                    else:
                        print("O número de casos precisa ser menor que o número de habitantes!")
                else:
                    print("Digite valores válidos!")

            # Adiciona as informações ao arquivo csv e a lista gerada no inicio do código
            write = csv.writer(csvfileW, delimiter=',')
            write.writerow([NewDate, bairro, habitantes, NewSuspeitos, NewNegativos, NewConfirmados])
            Lista.append([NewDate, bairro, habitantes, NewSuspeitos, NewNegativos, NewConfirmados])
            datas.add(NewDate)

        case "4":
            # Faz a comparação de dados, filtrada por data ou bairro, depende de qual o usuario escolher
            invalidComp = True
            while invalidComp:
                CompareOp = input("Qual parametro de comparação deseja usar?\n1- Bairro\n2- Data")
                if CompareOp == "1":
                    invalidComp = False
                    InvalidPam = True
                    while InvalidPam:
                        # Pede os dois parametros e checa se estão no sistema
                        filtro = input("Digite a primeiro bairro desejado: ")
                        filtro2 = input("Digite a segundo bairro desejado: ")
                        if usagedef.ValiBairro(filtro, bairros) and usagedef.ValiBairro(filtro2, bairros):
                            rowFilt = 1
                            InvalidPam = False
                        else:
                            print(f"Não há registros para esse bairro.\n")

                elif CompareOp == "2":
                    invalidComp = False
                    InvalidPam = True
                    while InvalidPam:
                        # Pede os dois parametros e checa se estão no sistema
                        filtro = input("Digite a data mais atual desejada(dd/mm/YYYY): ")
                        filtro2 = input("Digite a data mais antiga desejada(dd/mm/YYYY): ")
                        if usagedef.ValiDate(filtro, datas) and usagedef.ValiDate(filtro2, datas):
                            rowFilt = 0
                            InvalidPam = False
                        else:
                            print(f"Não há registros para essa data.\n")

                else:
                    print("Digite uma opção valida!")

            # Pega todos os casos do sistema, soma e armazena nas variaveis para fazer a impressão dos dados
            confSoma1 = sum([int(row[5]) for row in Lista if row[rowFilt] == filtro])
            confSoma2 = sum([int(row[5]) for row in Lista if row[rowFilt] == filtro2])
            negSoma1 = sum([int(row[4]) for row in Lista if row[rowFilt] == filtro])
            negSoma2 = sum([int(row[4]) for row in Lista if row[rowFilt] == filtro2])
            difNeg = abs(negSoma1 - negSoma2)
            difConf = abs(confSoma1 - confSoma2)

            # cria uma tabela com os dados e imprime a mesma
            Compare = [["Filtro", "Casos Negativos", "Casos positivos"],[filtro, negSoma1, confSoma1],[filtro2, negSoma2, confSoma2],["Direfença", difNeg, difConf],
                       ["Porcentagem", f"{round((difNeg/(negSoma1+negSoma2)*100), 0)}%", f"{round((difConf/(confSoma1+confSoma2)*100), 0)}%"]]
            
            print(tabulate(Compare, headers='firstrow', tablefmt='rounded_grid'))                    
              
        case "5":
            print("\nFinalizando programa")
        case _:
            print("\nSelecione uma opção válida!\n")

try:
    # fecha o arquivo após encerrar o programa, para assim atualizar o csv com os novos dados
    csvfileW.close()
except:
    print(IOError)