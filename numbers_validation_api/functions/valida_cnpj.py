import re

def regex_cnpj(cnpj):
    regex = re.compile("^[0-9]{14}$")
    return regex.match(cnpj)

def is_not_digitos_iguais(cnpj):
    not_can_be = ['11111111111111', '22222222222222', '33333333333333'
        '44444444444444', '55555555555555', '66666666666666',
        '77777777777777', '88888888888888', '99999999999999'
    ]
    return not(cnpj in not_can_be)

def primeiro_digito(cnpj):
    soma = 0
    contador = 5
    for digito in cnpj[:-2]:
        soma += int(digito) * contador
        if contador == 2:
            contador = 9
        else:
            contador -= 1
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto == int(cnpj[-2]):
        print('passou')
        return True
    else:
        return False

def segundo_digito(cnpj):
    soma = 0
    contador = 6
    for digito in cnpj[:-1]:
        soma += int(digito) * contador
        if contador == 2:
            contador = 9
        else:
            contador -= 1
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto == int(cnpj[-1]):
        print('passou')
        return True
    else:
        return False


def valida_cnpj(cnpj_str):
    cnpj = cnpj_str.replace(".", "").replace(" ", "")
    cnpj = cnpj.replace("-", "").replace("/", "")
    if (regex_cnpj(cnpj)):
        if ((is_not_digitos_iguais(cnpj)
            and primeiro_digito(cnpj))
            and segundo_digito(cnpj)):
            return True
        else:
            return False
    else:
        return False
    return True