"""Método de verificación, recibe un parámetro cualquiera y comprobará que sea
del tipo y tamaño requerido, los códigos de error son en el orden de los 500
porque es imposible que una operación dé como resultado un número en ese orden"""


def verificacion(op):

    # Se comprueba que sea de tipo entero
    if(isinstance(op, int)):

        # Se comprueba que se encuentre en el intervalo de restricción
        if(op > -127 and op < 127):
            return True, 0

        else:

            # Mensaje de error para estar fuera del intervalo
            print("El elemento es demasiado grande o demasiado pequeño")
            return False, 502
    else:

        # Mensaje de error de tipo de elemento
        print("El elemento no es de tipo entero")
        return False, 501


"""Método basic_ops, recibe 3 parámetros, dos operandos y el tipo de operación
por realizar. Para verificar el tipo de operando se llama el método verificación,
retorna el resultado si cumple la verificación. Caso contrario retornará el
resultado de la verificación de ambos operandos de manera que se logre ver cual
variable incumple y su codigo de error"""


def basic_ops(op1, op2, tipo):

    r1, r2 = verificacion(op1)
    r3, r4 = verificacion(op2)

    # Se comprueba que op1 cumpla
    if(r1):

        # Se comprueba que op2 cumpla
        if(r3):

            # Se verifica el tipo
            if(verificacion(tipo)):

                # Se verifica que se encuentre dentro del intervalo
                if(tipo > -1 and tipo < 4):

                    # Un switch para los casos
                    if(tipo == 0):
                        resultado = op1 + op2
                    elif(tipo == 1):
                        resultado = op1 - op2
                    elif(tipo == 2):
                        resultado = op1 & op2
                    elif(tipo == 3):
                        resultado = op1 | op2
                    return resultado

                else:

                    # Código de error para estar fuera del intervalo de operación
                    print("El tipo de operación seleccionada no es válida")
                    return 503

            else:

                # Código de error para tipo no entero
                print("El tipo de operación seleccionada no es un entero como se solicitó")
                return 503

        else:

            # Codigo de error para error en op2
            print("El segundo operando no es de tipo entero o es demasiado grande")
            return r4

    else:

        # Código de error para op1
        print("El primer operando no es de tipo entero o es demasiado grande")
        return r2


"""Método array_ops, recibe 3 parámetros, dos arreglos que deben se espera sean
del mismo largo, los elementos del arreglo deben ser del tipo entero y se
utilizará el metodo verificación para corroborar esto, finalmente se operarán
con el tipo de operación seleccionada, este ultimo parámetro(tipo) tambien será
verificado"""


def array_ops(ar1, ar2, tipo):

    # Se toma el largo de los arreglos, como son iguales con uno basta
    largo1 = len(ar1)

    # Se define el arreglo de sálida
    resultado = []

    # Se verifica que el párametro tipo sea de tipo entero
    if(verificacion(tipo)):

        # Que se encuentr dentro del intervalo correcto
        if(tipo > -1 and tipo < 4):

            # Se plantea un for que se repita un número de veces igual al arreglo
            for x in range(0, largo1):

                r1, r2 = verificacion(ar1[x])
                r3, r4 = verificacion(ar2[x])

                # Se verifican que las entradas x-ésimas de los arreglos cumplan con las caracteristicas
                if(r1):

                    if(r3):

                        # Si todo esto se cumple se añade al final del arreglo el resultado de operar las entradas
                        resultado.append(basic_ops(ar1[x], ar2[x], tipo))

                    else:
                        x = largo1
                        return r4

                else:
                    x = largo1
                    return r2

        else:

            # Código de error de tipo de operación inválida
            print("No se seleccionó un tipo de operación válida")
            return 503

    else:

        # Código de error cuando la operación es inválida
        print("El tipo de elemento para el selector de operación no es válida")
        return 503

    return resultado
