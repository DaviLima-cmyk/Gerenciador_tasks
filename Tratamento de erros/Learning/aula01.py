#ex01

Numbers = [3,5,6,2,9]


try:

    number = int(input())
    if number < 0 or number.isalpha():#bloco de codigo que verifica se a entrada e Negativa ou Se é um caractere
        raise ValueError('Era esperado um numero positivo')

except ValueError as e:
    print('Valor invalido,era esperado valor positivo ou um nao Caractere',e)

else:
    Numbers.append(number)

finally:
    print(Numbers)


