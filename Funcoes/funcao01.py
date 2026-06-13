def soma( x,y):   #criacao de funcao soma
    result = x + y
    return result #o que ela deve retornar
    

a = int(input())
b = int(input())
print("soma:",soma(a,b)) #chamada da funcao soma



# Lambda:

    # o lambda e usado quando queremos chamar pequenas funcoes,funcoes mais simples

    # Estrutura:

    # x = lambda parametros: o que fazer com os paramentros

    # Ex:

result = lambda x,y: x//y

t = int(input())
l = int(input())

print(result(t,l))



