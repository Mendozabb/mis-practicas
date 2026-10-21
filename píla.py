

pila = []


for i in range(1, 11):
    pila.append(f"Plato {i}")

print("Pila inicial:")
print(pila)


print("Plato en la cima:")
print(pila[-1])


print("Retirando 4 platos:")

for i in range(4):
    plato = pila.pop()
    print("Se retiro:", plato)

print("Pila despues de retirar 4 platos:")
print(pila)


print("Cantidad de platos restantes:", len(pila))
print("¿La pila esta vacia?", len(pila) == 0)

print("Vaciando la pila:")

while len(pila) > 0:
    print("Se retiro:", pila.pop())

print("Pila final:", pila)
print("¿La pila esta vacia?", len(pila) == 0)
