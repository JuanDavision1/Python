import hunspell
dic = hunspell.HunSpell("es_ANY.dic", "es_ANY.aff")
hola ='oye yo zoy una perzona fea'
nuevo = hola.split(" ")
print(nuevo)
for palabra in nuevo:
    print(palabra)
    print(dic.spell(palabra))
    if dic.spell(palabra) == False:
        print("Palabra Sugerida")
        arreglo = dic.suggest(palabra)
        print(arreglo[0])
