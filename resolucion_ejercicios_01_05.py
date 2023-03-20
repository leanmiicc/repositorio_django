########################   Ejercicio 1:   ########################
# Escribir una función que calcule el máximo común divisor entre dos números.

def calcular_maximo_comun_divisor(a,b):
    """calcula el maximo comun divisor entre dos números

    Args:
        a (int): numero entero
        b (int): numero entero

    Returns:
        int: resultado de maximo comun divisor
    """
    numedorador = 0
    while b != 0:
        numedorador = b
        b = a % b
        a = numedorador
    return a

print(calcular_maximo_comun_divisor(2,4))

########################   Ejercicio 2:   ########################
# Escribir una función que calcule el mínimo común múltiplo entre dos números

def calcular_minimo_comun_multiplo(a, b):
    """calcula el mínimo común múltiplo entre dos números

    Args:
        a (int): numero entero
        b (int): numero entero

    Returns:
        int: resultado de minimo comun multiplo
    """
    resultado_multiplicacion = a * b
    resultado_mcd = calcular_maximo_comun_divisor(a,b)
    resultado_mcm = resultado_multiplicacion / resultado_mcd
    return resultado_mcm

print(calcular_maximo_comun_divisor(2,4))

########################   Ejercicio 3:   ########################
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def get_diccionario_desde_cadena_caracteres(cadena_caracteres):
    """transforma una cadena de caracteres en un diccionario con la cantidad de veces que aparece cada palabra.
    Args:
        a (str): cadena de caracteres

    Returns:
        dict: dict de palabras con sus cantidades
    """
    dicc_palabras = dict()
    lista_palabras = cadena_caracteres.split()
    for palabra in lista_palabras:
        if palabra in dicc_palabras:
            dicc_palabras[palabra] += 1
        else:
            dicc_palabras[palabra] = 1
    return dicc_palabras

print(get_diccionario_desde_cadena_caracteres("hola mundo como estan mundo como"))

########################   Ejercicio 4:   ########################
# Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia

def get_tupla_from_diccionario(func):
    """ transforma un diccionar en una tupla con la cantidad de la palabra más repetida y su frecuencia
    Args:
        a (dict): diccionario

    Returns:
        tupla: tupla con la cantidad de la palabra más repetida y su frecuencia
    """
    tpl_cantidad_maxima = []
    for key, value in func.items():
        if value == max(func.values()):
            tpl_cantidad_maxima.append(key)
            tpl_cantidad_maxima.append(value)
    return tpl_cantidad_maxima

print(get_tupla_from_diccionario(get_diccionario_desde_cadena_caracteres("hola mundo como estan mundo como mundo como mundo como")))

########################   Ejercicio 5:   ########################
# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
# ejercicio tanto de manera iterativa como recursiva.

########################   Forma iterativa   ########################

def get_int():
    try:
        numero_entero = int(input("Ingrese un numero entero para la forma iterativa: "))
        while type(numero_entero) == int:
            print(f"El numero ingresado es: {numero_entero}")
            numero_entero = int(input("Ingrese un numero entero para la forma iterativa: "))
    except ValueError:
        print("No se ingreso un número.")

get_int()

########################   Forma recursiva   ########################

def get_int():
    try:
        numero_entero = int(input("Ingrese un numero entero para la forma recursiva: "))
        if type(numero_entero) == int:
            print(f"El numero ingresado es: {numero_entero}")
            get_int()
    except ValueError:
        print("No se ingreso un número.")

get_int()
