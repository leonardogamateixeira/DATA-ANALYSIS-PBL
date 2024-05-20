import csv

InvalidOp = True
while InvalidOp == True:
    menuOp = input('''\n1- Informações do sistema
2- Alterar dados
3- Sair

Selecione uma opção: ''')

    match menuOp:
        case "1":
            with open('denguedata.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in reader:
                    print(' '.join(row))
        case "2":
            escrever = input("Escreva: ")
            with open('some.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(escrever)
        case "3":
            print("\nFinalizando programa")
            exit()
        case _:
            print("\nSelecione uma opção válida!\n")

