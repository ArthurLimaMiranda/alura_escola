import re
from validate_docbr import CPF

def cpf_invalido(cpf):
    cpf_comp = CPF()
    cpf_valido = cpf_comp.validate(cpf)
    return not cpf_valido

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9][4]'
    celularOk = re.findall(modelo, celular)
    return not celularOk