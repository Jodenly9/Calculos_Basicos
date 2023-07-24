def main():
    """
    Ejecuta cuatro módulos que realizan cálculos y simulaciones en base a la interacción con el usuario.
    1. Coste de Hora: Calcula la paga correspondiente según las horas trabajadas y el coste por hora.
    2. Índice de Masa Corporal: Calcula el índice de masa corporal del usuario.
    3. Cuenta de Ahorros: Calcula el balance de una cuenta de ahorros con interés anual para varios años.
    4. Barra de Pan: Calcula el coste final a pagar por barras de pan vendidas, considerando descuentos por no ser frescas.
    """
    print("Ejercicio de Datos Simples")
    print("\n1. Coste de Hora")
    Coste_de_hora()
    print("\n2. Indice de Masa Corporal")
    Indic_masa_corporal()
    print("\n3. Cuenta de Ahorros")
    Cuenta_Ahorros()
    print("\n4. Barra de Pan")
    BarraPan()

def Coste_de_hora():
    print('Se calculará la paga corrrespondiente segun las horas trabajadas')
    print('y el coste por hora.')
    Hours_Worked= int(input('Ingrese las horas trabajadas: '))
    Coste_x_hora= int(input('Ingrese el coste por hora: '))
    resultado= Hours_Worked * Coste_x_hora
    print("El costo total es:", resultado)
    
def Indic_masa_corporal():
    print('Se calculará el índice de masa corporal del usuario.')
    peso = float(input('¿Cuál es tu peso en kg? '))
    altura =float(input('¿Cuál es tu altura en metros? '))
    imc= round(peso / (altura)**2, 2)
    print ('Tu índice de masa corporal es ',str(imc),'%')
    
def Cuenta_Ahorros():
    Dinero_en_cuenta_ahorros= float(input('¿Cuánto dinero tiene en su cuenta de ahorro? '))
    interes= float(input('Ingrese el  interes al año: '))/100
    years= int(input('¿Cuántos años desea calcular? '))
    balance= Dinero_en_cuenta_ahorros
    for year in range(1, years + 1):
        balance *= (1 + interes)
        print(f"Balance tras el año {year}: {round(balance, 2)}")

def BarraPan():
    barras= int(input("Introduce el número de barras vendidas que no son frescas: "))
    precio= 3.49 
    descuento= 0.6
    coste= barras * precio * (1 - descuento)
    print("El coste de una barra fresca es ", precio, "€")
    print("El descuento sobre una barra no fresca es ", descuento * 100, "%")
    print("El coste final a pagar es ", round(coste, 2), "€")

main()