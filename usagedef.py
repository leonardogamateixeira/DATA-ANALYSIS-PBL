from datetime import datetime
from datetime import timedelta
# função para validar as a entrada checando se existe esse valor na lista
def Validate(entrada, lista):
    if entrada in lista:
        return True
    else:
        return False
# função para validar as entradas de casos checando se são numeros
def ValiNum(suspeitos, negativos, confirmados):
    if suspeitos.isnumeric() and negativos.isnumeric() and confirmados.isnumeric() == True:
        return True
    else:
        return False
# função para aumentar um dia caso o usuario selecione a opção de adcionar dia
def DayAdd(LastDate):
    date = datetime.strptime(LastDate, "%d/%m/%Y")
    dateplus = date + timedelta(days=1)
    return dateplus.strftime("%d/%m/%Y")