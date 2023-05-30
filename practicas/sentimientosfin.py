import pandas as pd
import spacy
from spacy.lang.es.stop_words import STOP_WORDS


def sentence_segmentation(text):
    nlp = spacy.load("es_core_news_sm")
    doc=nlp(text)
    oraciones=[]
    for sent in doc.sents:
        oraciones.append(sent.text)
    return oraciones

def lemmatization(oraciones):
    nlp = spacy.load("es_core_news_sm")
    lemmatizer = nlp.get_pipe("lemmatizer")
    aux=[]
    for oracion in oraciones:
        doc = nlp(oracion)
        aux.append([token.lemma_ for token in doc])        
    return aux

def stop_word_removal(oraciones):
    aux=[]    
    for oracion in oraciones:
        aux2=[]
        for word in oracion:            
            if word not in STOP_WORDS:
                aux2.append(word)                 
        aux.append(aux2)
    return aux

def palabras_positivas():
    archivo=open("C:\\Intel\\palabras-positivas.txt",'r')
    palabras=[]
    for item in archivo.readlines():
        item=item.rstrip()
        palabras.append(item)
    positivo=set(palabras)
    return positivo

def palabras_negativas():
    archivo=open("C:\\Intel\\palabras-negativas.txt",'r')
    palabras=[]
    for item in archivo.readlines():
        item=item.rstrip()
        palabras.append(item)
    negativo=set(palabras)
    return negativo

if __name__=='__main__':
    ruta_datos="C:\\Intel\\comentarios.xlsx"    
    df = pd.read_excel(ruta_datos, sheet_name='Hoja1')        
    positivo = palabras_positivas()
    #print(positivo)
    negativo = palabras_negativas()    
    
    for id,dato in enumerate(df['Comentario']): 
        print(df['Numero de estrellas'][id])
        print(dato)
        oraciones=sentence_segmentation(dato)        
        #print(oraciones)
        oraciones=lemmatization(oraciones)        
        #print(oraciones)
        oraciones=stop_word_removal(oraciones)
        #print(oraciones)
        positivas=palabras_positivas()
        #print(positivas)
        negativas=palabras_negativas()
        #print(negativas)
        puntos_buenos=0
        puntos_malos=0
        for  oracion in oraciones:
            for palabra in oracion:
                if palabra in list(positivas):
                   puntos_buenos+=1
                   print ("+"+palabra)
                elif palabra in list(negativas):
                    puntos_malos+=1
                    print("-"+ palabra)
        total=puntos_buenos-puntos_malos
        print("puntos :", total)
        if total>=0:
            print("positivos")
        else:
            print("negativos")                
    print("Programa terminado")
    