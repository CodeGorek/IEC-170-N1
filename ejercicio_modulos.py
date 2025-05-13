# import : importa funciones de otros módulos math:libreria de funciones matemáticas
import math

# pi = 3.1416
pi = math.pi

# def fn_area_circunferencia(radio): define la función para calcular el area de la circunferencia
def area_circunferencia(radio):
    area = pi * radio ** 2
    return area
# def fn_raiz_cuadrada(numero): define la función para calcular la raíz cuadrada
def raiz_cuadrada(numero):
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada
# def fn_ejecutar_codigo(): define la función para ejecutar el código
def ejecutar_codigo():
    print()
    radio = float(input("Ingrese el radio de la círcunferencia: "))
    print()
    respuesta_1 = area_circunferencia(radio)
    numero = float(input("Ingrese un número: "))
    print()
    respuesta_2 = raiz_cuadrada(numero)

    print(f"El área de la círcunferencia de radio {radio} {respuesta_1}")
    print()
    print(f"La raíz cuadrada de {numero} es {respuesta_2}")
    print()

ejecutar_codigo()