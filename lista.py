# nota1 = 7.9
# nota2 = 9.7
# nota3 = 9.2

# notas = [7.9, 9.7, 8.2]

# lista = []
# lista = list()
# lista = [21, 'Luis', 1.333, True]
# lista_de_lista = [10, [1, 2, 3]]

# lista = [21, 'Luis', 1.333, True]

# print (lista[0])
# print (lista[1])
# print (lista[2])
# print (lista[3])

# print(lista[-1])
# print(lista[-2])
# print(lista[-3])
# print(lista[-4])

# lista = [10, 50, 30 , 40, 25, 60, 5]

# print(lista[0:3])
# print(lista[3:6])
# print(lista[3:])
# print(lista[2:6:2])

# for elemento in lista:
#     print(elemento)

# print('Quantidade de elememtos na lista: ', len(lista))

# for i in range(len(lista)):
#     print(i)

# for i in range(len(lista)):
#     print (lista[i])

lista = [1, 3, 12, 8, 2]

print('Lista padrão', lista)

lista.append(3)

print ('Lista pós Append', lista)

lista.insert(2, 10)

print('Lista pós Insert', lista)

lista2 = [1, 2, 3]
lista.extend(lista2)
print('Lista pós Extend', lista)

lista.pop()

print('Lista pós Pop', lista)

lista.pop(0)

print('Lista pós Pop', lista)

lista.remove(3)

print('Lista pós Remove', lista)


print('Quantidade de 2 na lista: ', lista.count(2))

print('Indice do elemento 12: ', lista.index(12))

lista.sort()
print('Lista pós Sort(crescente)', lista)

lista.sort(reverse=True)
print('Lista pós Sort(decrescente)', lista)

print(len(lista))

print(sum(lista))

print('Maior elemento da lista: ', max(lista))

print('Menor elemento da lista: ', min(lista))
