#!/usr/bin/env python2

from os import walk
import time
#from os import listdir
#from os.path import isfile, join


import fileinput
'''
def reader(path):
    buffer=""
    for line in fileinput.input(path):
        buffer+=line
    return buffer

def elementos(texto):
    buff=[]
    start=texto.find("Métodos")
    end=texto[start:len(texto)].find("\n")
    textov2=texto[start:end+start]
    buffer=""
    i=len(textov2)-1
    while(i>0):
        if(textov2[i]==" "):
            break
        buffer=textov2[i]+buffer
        i-=1

    return buffer.split(",")

def limpia(tokens):
    aLimpiar=[]
    for i in range(0,len(tokens)):
        if(tokens[i]==''):
            aLimpiar.append(i)
        elif(tokens[i][0]==' '):
            aLimpiar.append(i)
    aLimpiar.reverse()
    for i in aLimpiar:
        tokens.pop(i)
    return tokens

def agregaM(tokens):
    buffer=[]
    for i in tokens:
        j=0
        while(j<len(i)):
            if(i[j]=="m"):
                i[j-1]=i[j-1]+i[j]
            j+=1
        while(True):
            if ("m" in i):
                i.remove("m")
            else:
                break
        buffer.append(i)
    return buffer

def codigos(text):
    buffer=""
    i=len(text)-1
    while(i>0):
        if(text[i]=="L"):
            break
        buffer=text[i]+buffer
        i-=1
    tokens=buffer.split("\n")
    tokens=limpia(tokens)
    buffer=[]
    for i in tokens:
        buffer.append(limpia(i.split(" ")))
    tokensFinal=    agregaM(buffer)

    return tokensFinal


def maquina1(path):
    text=reader(path)

    elems=elementos(text)

    cod=codigos(text)
    print (elems,cod)
    for i in cod:
        print(i)

    #intex=text.find("CCV")
    #print(text)
    #print(text[intex:len(text)])
    #textoFiltrado=text[intex:len(text)].split("\n")
    #print(textoFiltrado)




def maquina2():
    text=reader("C:\\Users\\Carlos\\Desktop\\Proyecto\\texto\\azufre 14_05_14.txt")
    intex=text.find("\n")

    textoFiltrado=text[intex:len(text)].split("\n")
    textoFiltrado=limpia(textoFiltrado)

    buffer=[]

    for i in textoFiltrado:
        buffer.append(i.split("\t"))

    chosen=buffer[0][3]
    print(chosen,buffer)
'''

#maquina1()
#maquina2()
#print(reader("C:\\Users\\Carlos\\Desktop\\texto\\REPORT.TXT"))
#print(reader("C:\\Users\\Carlos\\Desktop\\texto\\S16_01-19"))
#print(reader("C:\\Users\\Carlos\\Desktop\\texto\\azufre 14_05_14.txt"))
import fileinput
''''''''''''''''odoo
'''
import functools
from xmlrpc import client

from builtins import print


def reader(path):
    buffer=""
    for line in fileinput.input(path):
        buffer+=line
    return buffer

HOST =  reader("Servidor.txt").split()[0]
PORT =  8069
DB =    'Laboratorio_De_Analisis_Agronomicos'
USER =  reader("Servidor.txt").split()[1]
PASS =  reader("Servidor.txt").split()[2]
ROOT =  'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login por defecto
uid = client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print ("Logged in as %s (uid:%d)" % (USER,uid))


models = client.ServerProxy(ROOT + 'object')
'''
'''''''''''''''''''''''''''''''''


def elementos(texto):
    buff=[]
    start=texto.find("Métodos")
    end=texto[start:len(texto)].find("\n")
    textov2=texto[start:end+start]
    buffer=""
    i=len(textov2)-1
    while(i>0):
        if(textov2[i]==" "):
            break
        buffer=textov2[i]+buffer
        i-=1

    return buffer.split(",")

def limpia(tokens):
    aLimpiar=[]
    for i in range(0,len(tokens)):
        if(tokens[i]==''):
            aLimpiar.append(i)
        elif(tokens[i][0]==' ' or tokens[i][0]=='\t'):
            aLimpiar.append(i)
    aLimpiar.reverse()
    for i in aLimpiar:
        tokens.pop(i)
    return tokens

def agregaM(tokens):
    buffer=[]
    for i in tokens:
        j=0
        while(j<len(i)):
            if(i[j]=="m" or i[j]=="Q"):
                i[j-1]=i[j-1]+i[j]
            j+=1
        while(True):
            if ("m" in i):
                i.remove("m")
            elif ("Q" in i):
                i.remove("Q")
            else:
                break
        buffer.append(i)
    return buffer

def codigos(text):
    buffer=""
    i=len(text)-1
    while(i>0):
        if(text[i]=="L" or text[i]=="%"):
            break
        buffer=text[i]+buffer
        i-=1
    tokens=buffer.split("\n")
    tokens=limpia(tokens)
    buffer=[]
    for i in tokens:
        buffer.append(limpia(i.split()))
    tokensFinal=    agregaM(buffer)

    return tokensFinal

def maquina1(path):
    #text=reader("C:\\Users\\Carlos\\Desktop\\Proyecto\\texto\\S16_01-19")
    text=reader(path)
    elems=elementos(text)

    cod=codigos(text)


    insertaM1 (elems,cod)

def insertaM1(e,c):

    for i in c:
        if (i[0]!='CCV'):
            for j in range(1,len(i)):

                id=models.execute_kw(DB, uid, PASS,
                'lab.result', 'search_read',
                [[['name', '=', 'M:'+i[0]+'__E:'+e[j-1]]]],
                {'fields': ['id']})
                if(id!=[]):
                    print("Se inserto: "+i[0]+"  "+e[j-1]+"  "+str(float(i[j].replace(",", "."))))
                    id=id[0]['id']
                    models.execute_kw(DB, uid, PASS, 'lab.result', 'write', [[int(id)], {
                        'valor': float(i[j].replace(",", "."))
                    }])
                else:
                    print("No se inserto: "+i[0])
    print("Si no se insertó compruebe si el código de la muestra está escrito correctamente")


def maquina2(path):
    text=reader(path)
    intex=text.find("\n")

    cual=text[0:intex].split()[7].split(",")[0].split(".")[0]
    print(cual)
    textoFiltrado=text[intex:len(text)].split("\n")
    buffer=[]
    for i in range(0,len(textoFiltrado)):
        if(textoFiltrado[i].split()!=[]):
            buffer.append(textoFiltrado[i].split())

    for i in buffer:
        if(cual=="660"):
            id=models.execute_kw(DB, uid, PASS,
                    'lab.result', 'search_read',
                    [[['name', '=', 'M:'+i[1]+'__E:P']]],
                    {'fields': ['id']})
        elif(cual=="420"):
            id=models.execute_kw(DB, uid, PASS,
                    'lab.result', 'search_read',
                    [[['name', '=', 'M:'+i[1]+'__E:S']]],
                    {'fields': ['id']})
        elif(cual=="430"):
            id=models.execute_kw(DB, uid, PASS,
                    'lab.result', 'search_read',
                    [[['name', '=', 'M:'+i[1]+'__E:B']]],
                    {'fields': ['id']})
        if(id!=[]):
            id=id[0]['id']
            models.execute_kw(DB, uid, PASS, 'lab.result', 'write', [[int(id)], {
                'valor': float(i[3].replace(",", "."))
            }])


def maquina3(path):
    print("Maquina 3, path: "+path)


def identificador(path):
    text=reader(path)
    text=text.split()
    if(text[0]=="Analista"):
        maquina1(path)
    elif(text[0]=="No."):
        maquina2(path)
    elif(True):
        print("Archivo no identificado favor contactar a gorr_03@hotmail.com")


def main():

	#Aqui pone la ruta de la carpeta donde se van a encontrar los archivos txt
	#Si se agregan archivos nuevos a esta ruta el programa los va a detectar
    mi_path = reader("Carpeta.txt")
	#Esto es una lista donde se guardan las rutas de los archivos
    files = []
    print("Esperando archivos...\n")
    while True:
        for (path, ficheros, archivos) in walk(mi_path):
            for i in archivos:
				#Aqui se comparan los archivos obtenidos por la ruta con los que ya se encuentran guardados
				#Si flag llega a ser 1 significa que el archivo ya fue agregado, si es 0 se agrega
                flag = 0
                for x in files:
                    rut2 = mi_path + "\\" + i
                    if(rut2 == x):
                        flag = 1
                if(flag == 0):
                    rut = mi_path + "\\" + i
                    identificador(rut)
                    print("Se analizo un nuevo archivo:\n"+i)

                    print("\nEsperando archivos...\n")
                    files.append(rut)


		#Intervalo de tiempo en el que el programa revisa si hay archivos nuevos
        time.sleep(3)



try:
    main()
except Exception as e:
    print (e)
    print("\n\n***Error***")

    print("Favor contactar a gorr_03@hotmail.com")
