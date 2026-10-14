estudiantes = ["Ana", "Carlos", "Diana"] 

print("1. Lista inicial: ", estudiantes)

estudiantes.append("Elena")
estudiantes.insert(1, "Beatriz")
print("2. lista tras inserciones: ", estudiantes)
print("Estudiante en el indice 0", estudiantes[0])
print("Estudiantes en el indice 2", estudiantes[2])
pos_diana = estudiantes.index("Diana")
print("Diana se encuentra en el indice", [pos_diana])
print("4. Resultados de Slicing: ")
primeros_3 = estudiantes[:3]
print("Primeros 3 estudiantes [:3]:", primeros_3)
subgrupo_1_3 = estudiantes[1:4]
print("Subgrupo del indice  1 al 3 [1:4]", subgrupo_1_3)
ultimos_2 = estudiantes[-2:]
print("Ultimos dos estudiantes [-2:]:", ultimos_2)
lista_invertida = estudiantes[::-1]
print("lista totalmente invertida [::-1]", lista_invertida)