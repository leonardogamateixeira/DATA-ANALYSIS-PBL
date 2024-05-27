from datetime import datetime
from datetime import timedelta
# função para validar as datas checando se existe uma data registrada com esse valor na lista unica (datas)
def ValiDate(data, datas):
    if data in datas:
        return True
    else:
        return False
# função para validar as os bairros checando se o bairro esta registrado na lista unica (bairros)
def ValiBairro(bairros, bairro):
    if bairro in bairros:
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