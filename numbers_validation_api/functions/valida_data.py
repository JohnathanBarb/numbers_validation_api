import datetime
def valida_data(ano, mes, dia):
    try:
        data = datetime.datetime(ano, mes, dia)
    except:
        return False
    
    return True