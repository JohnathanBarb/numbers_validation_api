import re

def regex_cpf(cpf):
    regex = re.compile("^[0-9]{11}$")
    return regex.match(cpf)

def primeiro_digito(cpf):
    soma = 0
    contador = 10
    for i in cpf[:-2]:
        soma += int(i) * contador
        contador -= 1
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto == int(cpf[-2]):
        return True
    else:
        return False

def segundo_digito(cpf):
    soma = 0
    contador = 11
    for i in cpf[:-1]:
        soma += int(i) * contador
        contador -= 1
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto == int(cpf[-1]):
        return True
    else:
        return False

def is_not_digitos_iguais(cpf):
    not_can_be = ['11111111111', '22222222222',
        '33333333333', '44444444444', '55555555555',
        '66666666666', '77777777777', '88888888888',
        '99999999999'
    ]
    return not (cpf in not_can_be)


def valida_cpf(cpf_str):
    cpf = cpf_str.replace(".", "").replace(" ", "").replace("-", "")
    if (regex_cpf(cpf)):
        if ((is_not_digitos_iguais(cpf)
            and primeiro_digito(cpf))
            and segundo_digito(cpf)):
            return True
        else:
            return False
    else:
        return False