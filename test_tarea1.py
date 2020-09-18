"""Prueba de las funciones creadas en Tarea_1.py mediante Pytest y Asserts"""

from Tarea_1 import*

def test_basic_ops():
    
    #Casos de éxito de basic_ops
    
    assert basic_ops(2,3,0) == 5
    assert basic_ops(5,2,1) == 3
    assert basic_ops(7,8,2) == 0
    assert basic_ops(7,8,3) == 15

    #Casos de error de basic_ops

    assert basic_ops('a',8,1) == 501 #Operando no entero
    assert basic_ops(129,8,1) == 502 #Operando demasiado grande
    assert basic_ops (8,8,7) == 503 #Seleccionador no soportado

def test_array_ops():

    #Se definen los arreglos

    arr1 = [1,2,3] #Arreglo correcto
    arr2 = [4,5,6] #Segundo arreglo correcto
    arr3 = ['a',5,6] #Error de tipo de elemento
    arr4 = [129,7,8] #Error de elemento demasiado grande

    #Casos de acierto

    assert array_ops(arr1,arr2,0) == [5,7,9]
    assert array_ops(arr1,arr2,1) == [-3,-3,-3]
    assert array_ops(arr1,arr2,2) == [0,0,2]
    assert array_ops(arr1,arr2,3) == [5,7,7]

    #Casos de error para array_ops

    assert array_ops(arr1,arr3,1)== 501 #Operando no entero
    assert array_ops(arr1,arr4,1)== 502 #Operando demasiado grande
    assert array_ops(arr1,arr2,5) == 503 #Sleccionador no soportado
