#Un atacante sabe que se ha empleado el cifrado César, pero no conoce el valor
#del desplazamiento
#alfabeto del 32 al 125 ASCII

ingles = set("""the be to of and a in that have i it for not on with he as you do at would
get could see look like can think come give say do will go make know take use work time person
year way day thing man world life part child eye woman
place work week case point government company""".split())

def rangoCaracteres(inicio,final):
    alf=""
    for letra in range(inicio,final+1):
        alf += chr(letra)
    return alf

def detectarCorimiento(mensaje):
    msg = mensaje.split(" ")
    for word in msg:
        if word in ingles:
            return True



def desifradoCesar(mensajecifrado):
    for corimiento in range(1,len(alfabeto)):
        mensaje = ""
        for letra in mensajecifrado[0]:
            if letra in alfabeto:
                indice = alfabeto.find(letra)
                indice -= corimiento
                if indice < 0:
                    indice += len(alfabeto)
                mensaje += alfabeto[indice]
            else:
                mensaje += letra
        if(detectarCorimiento(mensaje)):     
            print(f"corimiento es de : {corimiento} - {mensaje}")

if __name__=='__main__':
    alfabeto = rangoCaracteres(32,125)
    #print(alfabeto)
    entrada = open("C:\\Intel\\eng1.crp",'r')
    mensajecifrado = entrada.readlines()

    desifradoCesar(mensajecifrado)