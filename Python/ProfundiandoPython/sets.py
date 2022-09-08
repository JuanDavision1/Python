#profundiaR EN SETS
#coneccion de elementos unico y es mutables
#los elementos de un set deben ser inmutables
conjunto ={'juan', True,2,102}
print(conjunto)
#set vacio correcto
conjunto = set()
print(conjunto)
print(type(conjunto))
#mutable
conjunto.add('Juan')
print(conjunto)
#continee valores unicos no se duplican
conjunto.add('Juan')
print(conjunto)
#crear un ste apartir de un iterable
conjunto = set([4,3,5,2,4,5])
print(conjunto)
#podemos agregar mas elementos or incluso otro set
cpnjunto2={222,333,444,333,111}
conjunto.update(cpnjunto2)
print(conjunto)
conjunto.update([23,45,44,33])
print(conjunto)
#crear un set(copia poco profunda)
conjunto_copia=conjunto.copy()
print(conjunto_copia)
#verificar la igualdad
print(f'es igual en contenido?{conjunto == conjunto_copia}')
print(f'es igual referencia?{conjunto is conjunto_copia}')


#operaciones de conjuntos
#personas con distintas caracteristicas
pelo_negro ={'juan','karla','gg','maria'}
pero_rubio = {'lorenzo','marco','lau'}
ojos_cafe ={'karla','lau'}
menores_30años ={'juan','karla','maria'}
#union= todos los elementos de pelo cafe y rubio(no se repitem)
print(ojos_cafe.union(pero_rubio))
#interseccion , invertir el orden con el mismo resultado (conmutativo)
print(pero_rubio.union(ojos_cafe))

#interseccion Solo personasa on ojos cafe y pelo rubio
print(ojos_cafe.intersection(pero_rubio))

#diferencia pelo negro sin ojos color cafe
print(pelo_negro.difference(ojos_cafe))

#deferencia simetrica (regresa todos excepto los iguales en dos conjuntos)
print(pelo_negro.symmetric_difference(ojos_cafe))
#Conjuntos y subconjuntos
#preguntar si un set esta contenido en otro
#revisamos si los elementos del primer set estan contenidos estan contenidos en el segundo
print(menores_30años.issubset(pelo_negro))
#preguntar si un set contiene a otro set(superset)
#revisar si los elementos del priemr set estan contenidos en el segundo set
print(menores_30años.issuperset(pelo_negro))

#preguntar si los de pelo negro no tiene pelo rubio
print(pelo_negro.isdisjoint(pero_rubio))
