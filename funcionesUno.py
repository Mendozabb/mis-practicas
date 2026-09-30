import datetime
def saludar():
    print("Hola,Bienvenid@s")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print (f"La hora actual es: {hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base, altura):
    area= (base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print (f"El área del triángulo es: {resultado}")

def saludar_persona (nombre, edad):
    print (f"Hola {nombre}, tienes {edad} años")
saludar_persona("Raul", 19)

def calcular_imc(kg,altura):
    imc= (kg/altura)/2
    return imc
resultado=calcular_imc(65,1.77)
print(f"Tu imc es: {resultado}")

def incarte_al_mejor_del_mundo(futbolista,numero):
    print(f"Hola{futbolista}, tienes el numero {numero} numero")
incarte_al_mejor_del_mundo("Leonel Messi", 11)

def mensaje_para_messi():
    print("El mejor del mundo sin duda alguna, !VAMOS LEO¡")
mensaje_para_messi()