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
            escrever = input("Escreva: ")
            with open('some.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(escrever)
        case "4":
            print("\nFinalizando programa")
            exit()
        case _:
            print("\nSelecione uma opção válida!\n")