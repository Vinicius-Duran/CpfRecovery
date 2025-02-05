from itertools import product

def calcula_digitos_verificadores(cpf_base):
    cpf_base = [int(x) for x in cpf_base]
    
    # Primeiro dígito verificador
    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum([cpf_base[i] * peso1[i] for i in range(9)])
    digito1 = (soma1 * 10) % 11
    if digito1 == 10:
        digito1 = 0
    
    # Segundo dígito verificador
    peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum([cpf_base[i] * peso2[i] for i in range(9)]) + (digito1 * 2)
    digito2 = (soma2 * 10) % 11
    if digito2 == 10:
        digito2 = 0
    
    return str(digito1) + str(digito2)

def gerar_combinacoes_validas(cpf_parcial):
    cpf_base = cpf_parcial.replace(".", "").replace("-", "").replace("*", "")
    indices_asteriscos = [i for i, char in enumerate(cpf_parcial) if char == "*"]
    
    combinacoes_validas = []
    for comb in product("0123456789", repeat=len(indices_asteriscos)):
        cpf_completo = list(cpf_parcial)
        for i, index in enumerate(indices_asteriscos):
            cpf_completo[index] = comb[i]
        
        cpf_completo_str = "".join(cpf_completo).replace(".", "").replace("-", "")
        cpf_base_9 = cpf_completo_str[:9]
        digitos_verificadores = calcula_digitos_verificadores(cpf_base_9)
        
        if cpf_completo_str[-2:] == digitos_verificadores:
            combinacoes_validas.append("".join(cpf_completo))
    
    return combinacoes_validas

cpf_parcial = "505.44*.*08-0*"
combinacoes_validas = gerar_combinacoes_validas(cpf_parcial)

# Exibe algumas combinações válidas
print(combinacoes_validas[:10])  # Exibe as primeiras 10 combinações válidas (mudar o [10] caso queira ou precisa de mais combinações)
