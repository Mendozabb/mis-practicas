lista = [1,2,4,5,200,7,9]

for i in range(1, len(lista)):
    aux = lista[i]
    j = i-1
    while j>=0 and aux<lista[j]:
        lista[j+1]=lista[j]
        lista[j]=aux
        j-=1
print(lista)        