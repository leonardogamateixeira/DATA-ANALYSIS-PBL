from datetime import datetime
from datetime import timedelta

def ValiDate(filtro, datas):
    if filtro in datas:
        return True
    else:
        return False

def ValiBairro(bairros, bairro):
    if bairro in bairros:
        return True
    else:
        return False
    
def ValiNum(suspeitos, negativos, confirmados):
    if suspeitos.isnumeric() and negativos.isnumeric() and confirmados.isnumeric() == True:
        return True
    else:
        return False

def DayAdd(LastDate):
    date = datetime.strptime(LastDate, "%d/%m/%Y")
    dateplus = date + timedelta(days=1)
    return dateplus.strftime("%d/%m/%Y")