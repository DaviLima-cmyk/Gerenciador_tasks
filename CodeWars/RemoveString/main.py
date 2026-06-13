def RemoveLastandBeginStr(word):
    try:
        if len(word) <= 2:
            raise ValueError('Valor invalido')
    except ValueError as e:
        print(f'Size of string inconsistance {e}')

    else:
        var = word
        lista = list(var)
        for key in lista:
            if key == lista[0]:
                lista.pop(0)
                lista.pop(-1)
    finally:
        print(lista)
                

RemoveLastandBeginStr('criolo')