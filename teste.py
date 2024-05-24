import csv
from datetime import datetime
import usagedef
import tabulate

try:
    csvfileW = open('denguedata.csv', 'a')
    csvfileR = open('denguedata.csv', 'r')
    reader = csv.reader(csvfileR, delimiter=',')
except:
    print(IOError)

Lista = [row for row in reader]
csvfileR.close()

InvalidFilt = True
while InvalidFilt == True:
    filtro = input("\n1- Data\n2- Bairro\nPor qual parâmetro deseja buscar as informações?: ")
    match filtro:
        case "1":
            filtro = False
            while filtro == False:
                filtro = input("Digite a data desejada(dd/mm/YYYY): ")
                validation = usagedef.ValiDate(filtro)
                if validation == True:
                    rowFilt = 0
                    InvalidFilt = False
                else:
                    print(f"Não há registros para essa data.")
                    filtro = False
        case "2":
            filtro = False
            while filtro == False:
                bairros = set([row[1] for row in Lista])
                filtro = input("Digite o bairro desejado: ")
                if filtro in bairros:
                    rowFilt = 1
                    InvalidFilt = False
                else:
                    print(f"Não há registros para o bairro {filtro}")
                    filtro = False
        case _:
            print("Digite uma opção valida!")

TableFilt = [row for row in Lista if row[rowFilt] == filtro]
print(tabulate.tabulate(TableFilt, headers='firstrow', tablefmt='rounded_grid'))       
