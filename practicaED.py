def mostrar_encabezado_escuela():
    print(f"UNIVERSIDAD TECNOLOGICA DE XICOTEPEC DE JUAREZ")
    print(F"REGISTRO DE EVALUACIÓN DE CALIFICACIONES")
mostrar_encabezado_escuela()

def obtener_nota_minima_aprobatoria():
    return 6.0
obtener_nota_minima_aprobatoria()


def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif nota_final <= 9.4:
        return "Aprobado"
    else: 
        return "Excelente"
resultado = evaluar_rendimiento(8)
print(resultado)

def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)
    
def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado = evaluar_rendimiento(nota_final)

    print("==================================")
    print("Boleta de Calificaciones")
    print("Nombre del alumno: ", nombre_alumno)
    print("Nota de examen: ", nota_examenes)
    print("Nota de tareas: ", nota_tareas)
    print("Estado academico: ", estado)
    print("==================================")

    if nota_final < nota_minima:
        print("Debe presentar examen extraordinario")
    else:
        print("No presenta examen extraordinario")

mostrar_encabezado_escuela()
generar_boleta("Francisco Mendoza", 8.5, 9.0)
        
