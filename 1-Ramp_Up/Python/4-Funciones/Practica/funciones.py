
def piramide(n:int):
    n = int(n)
    lista_8 = list(range(n,0,-1))
    # print(lista_8)

    while len(lista_8) > 0:
        print(*lista_8)
        lista_8.pop(0)

def dia_semana(dia:int):
    match dia:
        case 1:
            out = "Lunes"
        case 2:
            out = "Martes"
        case 3:
            out = "Miércoles"
        case 4:
            out = "Jueves"
        case 5:
            out = "Viernes"
        case 6:
            out = "Sábado"
        case 7:
            out = "Domingo"
        case _:
            out = "Día de la semana erróneo"
    # print(out)
    return out

def ejercicio_3(n_1, n_2):
    if n_1 == n_2:
        msg = "Son iguales"
    elif n_1 > n_2:
        msg = "Primer valor superior a segundo valor"
    else:
        msg = "Segundo valor superior a primer valor"
         
    return msg