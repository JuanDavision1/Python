numero = range(10)
lista_pares =[]
#creamos una nueva lista con los valores pares
for numero in numero:
    #revismaos si es par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista Pares:{lista_pares}')

#hacemos lo mismo pero con list comprenshensions
