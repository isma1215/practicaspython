alfabeto=" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}"
entrada = open("C:\\Intel\\eng1.crp",'r')
cifrado = entrada.read()

clave = 24

mensaje = ""

for letra in cifrado:
    if letra in alfabeto:
        indice = alfabeto.find(letra)
        indice -= clave
        if indice < 0:
            indice += len(alfabeto)
        mensaje += alfabeto[indice]
    else:
        mensaje += letra
print(mensaje)