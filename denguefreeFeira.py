# Autor: Leonardo Gama Teixeira
# Componente Curricular: 2024.1 EXA854 - MI - ALGORITMOS (TP03) 
# Concluido em: 01/05/2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

import csv
from tabulate import tabulate
import usagedef
# Abre o arquivo e armazena em variaveis duas funções, uma para ler o arquivo e outra adicionar para adicionar uma linha ao final dele
try:
    csvfileW = open('denguefreeFeira.csv', 'a', newline='')
    csvfileR = open('denguefreeFeira.csv', 'r')
    reader = csv.reader(csvfileR, delimiter=',')
except FileExistsError | FileNotFoundError:
    print("Arquivo não encontrado")

menuOp = ''  

InvalidLine = [row for row in reader if len(row) != 6]
Lista = [['Data','Bairros','Habitantes','Casos Suspeitos','Casos Negativos','Casos Confirmados'],[ '22/03/2024','Tomba',55007,100,20,500]]
if InvalidLine:
    print("Arquivo não corresponde aos parametros previstos, separe os itens em 6 colunas separados por virgula\n")
    print('Tabela exemplar')
    print(tabulate(Lista, tablefmt='rounded_grid'))
    menuOp = "4"

Lista = [row for row in reader]
datas = set([row[0] for row in Lista])
bairros = set([row[1] for row in Lista])
csvfileR.close()

if Lista == []:
     print("\narquivo vazio, crie um novo arquivo na opção 3(Adcionar informações)")
     Lista = ['Data','Bairros','Habitantes','Casos Suspeitos','Casos Negativos','Casos Confirmados']

while menuOp != "4":
    menuOp = input("\n  ----------Menu Inicial----------\n1- Buscar informações do sistema\n2- Ler arquivo\n3- Adcionar informações\n4- Sair\nSelecione uma opção: ")
    # Cria uma lista com informações unicas baseado em todos os bairros cadastrados

    bairroCasos = set()
    RecentCases = []
    for row in reversed(Lista):
        if row[1] in bairroCasos:
            continue
        RecentCases.append(row)
        bairroCasos.add(row[1])

    match menuOp:
        case "1":
            while menuOp == "1":
                BuscaOp = input("Como deseja fazer essa pesquisa?\n1- Comparando dois parâmetros\n2- Observando um pârametro expecifico")
                match BuscaOp:
                    case "1":
                             
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
                                    if usagedef.Validate(filtro, bairros) and usagedef.Validate(filtro2, bairros):
                                        rowFilt = 1
                                        InvalidPam = False
                                        nome = "Bairros"
                                    else:
                                        print(f"Não há registros para esse bairro.\n")

                            elif CompareOp == "2":
                                invalidComp = False
                                InvalidPam = True
                                while InvalidPam:
                                    # Pede os dois parametros e checa se estão no sistema
                                    filtro = input("Digite a primeira data que deseja comparar(dd/mm/YYYY): ")
                                    filtro2 = input("Digite a segunda data(dd/mm/YYYY): ")
                                    if usagedef.Validate(filtro, datas) and usagedef.Validate(filtro2, datas):
                                        nome = "Datas"
                                        rowFilt = 0
                                        InvalidPam = False
                                        RecentCases = Lista
                                    else:
                                        print(f"Não há registros para essa data.\n")

                            else:
                                print("Digite uma opção valida!")

                        # Pega todos os casos do sistema, soma e armazena nas variaveis para fazer a impressão dos dados
                            
                        confSoma1 = sum([int(row[5]) for row in RecentCases if row[rowFilt] == filtro])
                        confSoma2 = sum([int(row[5]) for row in RecentCases if row[rowFilt] == filtro2])
                        NegSoma1 = sum([int(row[4]) for row in RecentCases if row[rowFilt] == filtro])
                        NegSoma2 = sum([int(row[4]) for row in RecentCases if row[rowFilt] == filtro2])
                        difNeg = abs(NegSoma1 - NegSoma2)
                        difConf = abs(confSoma1 - confSoma2)
                        # cria uma tabela com os dados e imprime a mesma    

                        Compare = [[nome, "Casos Negativos", "Casos positivos"],
                           [filtro, NegSoma1, confSoma1],
                           [filtro2, NegSoma2, confSoma2],
                           ["Direfença", difNeg, difConf],
                           ["Diferença Percentual", f"{round((difNeg/(NegSoma1+NegSoma2)*100))}%", f"{round((difConf/(confSoma1+confSoma2)*100))}%"]]                               
                        print(tabulate(Compare, headers='firstrow', tablefmt='rounded_grid'))
                        menuOp = 0        
                    case "2":
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
                                        if usagedef.Validate(filtro, datas):
                                            rowFilt = 0
                                            InvalidPam = False
                                            InvalidFilt = False
                                            RecentCases = Lista
                                        else:
                                            print(f"Não há registros para essa data.")

                                case "2":
                                    InvalidPam = True
                                    while InvalidPam:
                                        # o usuario digita um bairro e o programa checa se esse bairro está cadastrado no arquivo
                                        filtro = input("Digite o bairro desejado: ")
                                        if usagedef.Validate(filtro, bairros):
                                            rowFilt = 1
                                            InvalidPam = False
                                            InvalidFilt = False
                                        else:
                                            print(f"Não há registros para o bairro {filtro}")

                                case _:
                                    print("Digite uma opção valida!")
                        
                            TableFilt = [row for row in Lista if row[rowFilt] == filtro]    
                            print(tabulate(TableFilt, headers=['Data','Bairro','Habitantes','Casos Suspeitos','Casos Negativos','Casos Confirmados'], tablefmt='rounded_grid'))
                            menuOp = 0                             
                        
        case "2":
            while menuOp == "2":
                PrintOp = input("Quais dados deseja acessar?\n1- Tabela completa\n2- Porcentagem de casos por bairro")
                if PrintOp == "1":    
                    RecentSus = sum([int(row[3]) for row in RecentCases[:-2]])
                    RecentNeg = sum([int(row[4]) for row in RecentCases[:-2]])
                    RecentConf = sum([int(row[5]) for row in RecentCases[:-2]])
                    ListaTotal = [['Total de casos notificados', 'Percentual de Suspeitos','Percentual de confirmados', 'Percentual de negativados'],[RecentConf+RecentNeg+RecentSus,f"{round((RecentSus/(RecentConf+RecentNeg+RecentSus)*100))}%",f"{round((RecentNeg/(RecentConf+RecentNeg+RecentSus)*100))}%",f"{round((RecentConf/(RecentConf+RecentNeg+RecentSus)*100))}%"]]
                    print(tabulate(Lista, headers='firstrow', tablefmt='rounded_grid'))
                    print(tabulate(ListaTotal, headers='firstrow', tablefmt='rounded_grid'))
                    menuOp = 0
                elif PrintOp == "2":
                    TablePorcent = []
                    for row in Lista[1:]:
                        pou = [row[1],f"{round(((int(row[3])/int(row[2]))*100), 1)}%",f"{round(((int(row[3])/int(row[2]))*100), 1)}%",f"{round(((int(row[5])/int(row[2]))*100), 1)}%"]
                        TablePorcent.append(pou)
                    print(tabulate(TablePorcent, headers=['Bairro','Percentual de suspeitos','Percentual de negativados','Percentual de confirmados' ], tablefmt='rounded_grid')) 
                    menuOp = 0  
                else:
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
                if usagedef.Validate(bairro, bairros):
                    habitantes = [row[2] for row in Lista if row[1] == bairro].pop()
                    InvalidLocale = False
                else:
                    print(f"\nNão é possivel registrar o bairro {bairro} pois não consta no sistema.\n")
                    BairroOp = input("Deseja adcionar um bairro ao sistema?\n1- Sim\n2- Não")
                    if BairroOp == "1":
                        bairro = input("Digite o nome do novo bairro: ")
                        habitantes = input("Digite a quantidade de habitantes no bairro: ")
                        if habitantes.isnumeric():
                            InvalidLocale = False
                        else:
                            print("Digite um valor numerico!")

                        
                    elif BairroOp == "2":
                        print("Ao inserir novos dados, certifique-se de que o bairro consta no sistema")
                    else:
                        print("Digite um valor válido")
                        
            InvalidNum = True
            while InvalidNum:
                # Pede a atualização dos dados do bairro no dia e checa se os valores digitados são validos
                suspeitos = input(f"Quantidade de novos casos suspeitos em {bairro}: ")
                negativos = input(f"Quantidade de novos casos negativos em {bairro}: ")
                confirmados = input(f"Quantidade de novos casos confirmados em {bairro}: ")

                if suspeitos.isnumeric() and negativos.isnumeric() and confirmados.isnumeric():
                    suspeitos, negativos, confirmados = list(map(int, [suspeitos, negativos, confirmados]))
                    # após a checagem checa se a soma dos casos não é maior que a quantidade de 
                    # habitantes do bairro e se a quantidade de casos negativos e confirmados não
                    # é maior que a quantidade de suspeitos anterior, caso não seja adiciona os casos a conta
                    if (suspeitos + negativos + confirmados) <= int(habitantes):
                        if bairro in bairros:
                            LastSuspeitos = int([row[3] for row in Lista if row[1] == bairro].pop())
                            NewNegativos = int([row[4] for row in Lista if row[1] == bairro].pop()) + negativos
                            NewSuspeitos = (LastSuspeitos + suspeitos) - (negativos + confirmados)
                            NewConfirmados = int([row[5] for row in Lista if row[1] == bairro].pop()) + confirmados
                        else:
                            LastSuspeitos = NewSuspeitos = suspeitos
                            NewNegativos = negativos
                            NewConfirmados = confirmados
                            
                        if negativos + confirmados < LastSuspeitos:
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
            print("\nFinalizando programa")
        case _:
            print("\nSelecione uma opção válida!\n")

# fecha o arquivo após encerrar o programa, para assim atualizar o csv com os novos dados
csvfileW.close()