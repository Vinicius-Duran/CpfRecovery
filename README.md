# CPF Recovery

Este código permite gerar combinações válidas de CPF a partir de um CPF parcial, onde alguns dígitos estão ocultos (representados por asteriscos). 
Ele usa a fórmula oficial para calcular os dois dígitos verificadores do CPF e verifica se as combinações geradas são válidas. 
A função gerar_combinacoes_validas gera todas as combinações possíveis substituindo os asteriscos por números, enquanto a função calcula_digitos_verificadores 
calcula os dígitos verificadores com base nos 9 primeiros números do CPF. O código retorna uma lista com as combinações válidas.

English:
This code generates valid CPF combinations from a partial CPF, where some digits are hidden (represented by asterisks). 
It uses the official CPF formula to calculate the two check digits and verifies if the generated combinations are valid. 
The gerar_combinacoes_validas function generates all possible combinations by replacing the asterisks with numbers, while the calcula_digitos_verificadores 
function calculates the check digits based on the first 9 digits of the CPF. The code returns a list of valid combinations.
