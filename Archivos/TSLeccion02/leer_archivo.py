
archivo = open('prueba.txt', 'r', encoding='utf8') # Las letras son: 'r' read, 'a' append, 'w' write, 'x'
# print(archivo.read())
# print(archivo.read(15))
# print(archivo.read(5)) # Continuamos desde la linea anterior
# print(archivo.readline())
# print(archivo.readline())

# Vamos a iterar el archivo, cada una de las lineas
# for linea in archivo:
    # print(linea): iteramos todos los elementos
# print(archivo.readlines()[1]) # accedemos al archivo como una lista

# Anexamos informacion  copiamos a otro
archivo2 =open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close() # cerramos el sagundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')
