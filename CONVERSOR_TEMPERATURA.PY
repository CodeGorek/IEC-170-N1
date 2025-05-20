#sistema de conversion de temperatura entre distintas escalas, celsius,fehrenheit y kelvin.
#1.-contruir menu 
#2.-definir funciones de conversion
#3.-pedir datos al usuario
#4.-realizar conversion
#5.-mostrar resultado

# °C °K = T + 273.15
# °C °F = T * 1.8 + 32
# °K °C = T - 273.15
# °K °F = (T - 273.15) * 1.8 + 32
# °F °C = (°F - 32) / 1.8
# °F °K = (T - 32)*5/9 + 273.15

def cargar_menu():
    print("[1]convertir °C a °K.")
    print("[2]convertir °C a °F.")
    print("[3]convertir °K a °C.")
    print("[4]convertir °K a °F.")
    print("[5]convertir °F a °C.")
    print("[6]convertir °F a °K.")  
    print("[0]salir.")

def convertir_CK(temperatura_inicial):
    temperarura = temperatura_inicial + 273.15
    return temperarura
    
def convertir_CF(temperatura_inicial):
    temperatura = temperatura_inicial * 1.8 + 32
    return temperatura
    
def convertir_KC(temperatura_inicial):
    temperatura = temperatura_inicial - 273.15
    return temperatura

def convertir_KF(temperatura_inicial):
    temperatura = (convertir_KC(temperatura_inicial)) * 1.8 + 32
    return temperatura

def convertir_FC(temperatura_inicial):
    temperatura = (temperatura_inicial - 32) / 1.8
    return temperatura

def convertir_FK(temperatura_inicial):
    temperatura = (convertir_FC(temperatura_inicial)) + 273.15
    return temperatura
 
def solicitar_datos():
    temperatura_usuario = float(input("Ingrese la temperatura a convertir: "))
    return temperatura_usuario

def programa_principal():
    print("Súper conversor de temperaturas!!")
    print("=================================")
    
    while True:
        cargar_menu()
        opcion = input("Ingrese una opción [0-6]: ")
        resultado = 0
        temperatura_inicial = 0
        escala_inicial = ""
        escala_final = ""

        if opcion == "1":
            escala_inicial = "°C"
            escala_final = "K"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_CK(temperatura_inicial)
        elif opcion == "2": 
            escala_inicial = "°C"
            escala_final = "°F"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_CF(temperatura_inicial)
        elif opcion == "3":
            escala_inicial = "K"
            escala_final = "°C"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_KC(temperatura_inicial)
        elif opcion == "4":
            escala_inicial = "K"
            escala_final = "°F"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_KF(temperatura_inicial)
        elif opcion == "5":
            escala_inicial = "°F"
            escala_final = "°C"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_FC(temperatura_inicial)
        elif opcion == "6":
            escala_inicial = "°F"
            escala_final = "K"
            temperatura_inicial = solicitar_datos()
            resultado = convertir_FK(temperatura_inicial)
        elif opcion == "0":
            print("Gracias por usar el conversor de temperaturas.")
            break #rompe la repeticion y sale del programa
        else:
            print("Opción no válida. Intente nuevamente.")
            print()
            pass
        print()
        print(f"{temperatura_inicial}{escala_inicial} = {resultado}{escala_final}")
        print()
    
programa_principal()
