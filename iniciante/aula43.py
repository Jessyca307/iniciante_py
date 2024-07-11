import random
for _ in range(100):
        cpf = ''
        nove_digitos = ''
        for i in range(9): 
               nove_digitos += str(random.randint(0, 9))

        contador_r = 10

        resultado = 0
        for digito_ in nove_digitos:
                resultado += int(digito_) * contador_r
                resultado -= 1

        digito_2 = (resultado * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_2)
        contador_r_2 = 11

        resultado_2 = 0
        for digito in dez_digitos:
                resultado_2 += int(digito) * contador_r_2
                contador_r_2 -= 1

        digito_3 = (resultado_2 * 10) % 11
        digito_3 = digito_3 if digito_3 <= 9 else 0
        novo_cpf = str(digito_2) + str(digito_3)
        digito_final = int(novo_cpf)
        print(digito_final)

        cpf_gerado_p_c = f'{nove_digitos}{digito_2}{digito_3}'
        print(cpf_gerado_p_c)