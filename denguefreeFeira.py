import csv

InvalidOp = True
while InvalidOp == True:
    menuOp = input('''1- Sobre a dengue
2- Analise dos dados
3- Sair

Selecione uma opção: ''')

    match menuOp:
        case "1":
            print("\nDengue q sei oq n sei oq la")
            InvalidOp = False
        case "2":
            print("\n(arquivo .csv, alterar adicionar e tals)")
            InvalidOp = False
        case "3":
            print("\nFinalizando programa")
            exit()
        case _:
            print("\nSelecione uma opção válida!\n")

print("\nfim")