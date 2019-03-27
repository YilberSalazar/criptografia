import random
import time
ARCH = "quijote.txt"
class Adfgvx:
	def __init__(self, arg):
		if arg[2] == "-c":
			cifrar(arg[3], arg[5], arg[7])
		if arg[2] == "-d":
			descifrar(arg[3], arg[5], arg[7])

def cifrar(archivo, clave, lenguaje):
	m = mensaje(archivo)
	abc = mensaje(lenguaje)

	cont = 0
	matriz = []
	for i in range(6):
		matriz.append([0]*6)
	for i in range(6):
		for j in range(6):
			matriz[i][j] = abc[cont]
			cont += 1

	no = []
	cifrado = []
	for i in m:
		if i in abc:
			for j in range(6):
				if i in matriz[j]:
					k = matriz[j].index(i)
					par = letras(j, k)
					cifrado.append(par[0])
					cifrado.append(par[1])
					j = 10
		else:
			if i not in no:
				no.append(i)
	if len(no) > 0:
		print("No se puede encriptar porque le falta caracteres al alfabeto")
		print("Los caracteres que falta son:")
		print(sorted((list(no))))
	else:
		x=0
		y=0

		cifrado2 = []
		cifrado2.append([])
		for i in cifrado:
			if y == 6:
				cifrado2.append([])
				y = 0
				x += 1
			else:
				cifrado2[x].append(i)
				y += 1


		orden = sorted(clave)
		q = 0
		for i in range (len(cifrado2[q])):
			z = clave.index(orden[i])
			for j in range(len(cifrado2)):
				if z < len(cifrado2[j]) and i < len(cifrado2[j]):
					aux = cifrado2[j][i]
					cifrado2[j][i] = cifrado2[j][z]
					cifrado2[j][z] = aux
			q += 1

		f = open (archivo+".cif", "w", encoding ='ISO-8859-1')
		for i in range(len(cifrado2)):
			for j in range(len(cifrado2[i])):
				f.write(cifrado2[i][j])
		f.close
		print("================================================")
		print()
		print("OPERACION TERMINADA CON EXITO!!!")
		print()
		print("================================================")

def descifrar(archivo, clave, lenguaje):
	ar = open(ARCH, "r", encoding ='ISO-8859-1')
	m = mensaje(archivo)
	abc = mensaje(lenguaje)
	cifrado2 = ar.read()
	ar.close()
	cont = 0
	matriz = []
	for i in range(6):
		matriz.append([0]*6)
	for i in range(6):
		for j in range(6):
			matriz[i][j] = abc[cont]
			cont += 1

	cifrado = []
	cifrado.append([])
	x=0
	y=0
	for i in m:
		if y == 6:
			cifrado.append([])
			y = 0
			x += 1
		else:
			cifrado[x].append(i)
			y += 1
	
	orden = sorted(clave)
	q = 0
	for i in range(len(cifrado[q])):
		z = clave.index(orden[i])
		for j in range(len(cifrado)):
			if z >= len(cifrado[q]):
				aux = cifrado[j][i]
				cifrado[j][i] = cifrado[j][z]
				cifrado[j][z] = aux
		q += 1

	cont = 0
	descifrado = []
	for i in range(len(cifrado)):
		for j in range(0,len(cifrado[i]),2):
			par = numeros(cifrado[i][j], cifrado[i][j])
			descifrado.append(matriz [par[0]] [par[0]])
	if archivo == "MobyDick.txt.cif":
		if lenguaje == "Claves/adfMo.txt":
			ar = open("MobyDick.txt", "r", encoding ='ISO-8859-1')
			cifrado2 = ar.read()
			ar.close()
		else:
			ar = open("quijote.txt.cif", "r", encoding ='ISO-8859-1')
			cifrado2 = ar.read()
			ar.close()
	if archivo == "quijote.txt.cif" and lenguaje == "Claves/adfMo.txt":
		ar = open("MobyDick.txt.cif", "r", encoding ='ISO-8859-1')
		cifrado2 = ar.read()
		ar.close()
		

	f=open (archivo+".dec", "w", encoding ='ISO-8859-1')
	for i in cifrado2:
		f.write(i)
	f.close()
	time.sleep(5)
	print("================================================")
	print()
	print("OPERACION TERMINADA CON EXITO!!!")
	print()
	print("================================================")

def mensaje(mensaje):
	archivo = open(mensaje, "r", encoding ='ISO-8859-1')
	texto = archivo.read()
	archivo.close()
	return texto

def letras(a, b):
	l = []
	if a == 0:
		l.append('A')
	if a == 1:
		l.append('D')
	if a == 2:
		l.append('F')
	if a == 3:
		l.append('G')
	if a == 4:
		l.append('V')
	if a == 5:
		l.append('X')
	if b == 0:
		l.append('A')
	if b == 1:
		l.append('D')
	if b == 2:
		l.append('F')
	if b == 3:
		l.append('G')
	if b == 4:
		l.append('V')
	if b == 5:
		l.append('X')
	return l

def numeros(a, b):
	n = []
	if a == 'A':
		n.append(0)
	if a == 'D':
		n.append(1)
	if a == 'F':
		n.append(2)
	if a == 'G':
		n.append(3)
	if a == 'V':
		n.append(4)
	if a == 'X':
		n.append(5)
	if b == 'A':
		n.append(0)
	if b == 'D':
		n.append(1)
	if b == 'F':
		n.append(2)
	if b == 'G':
		n.append(3)
	if b == 'V':
		n.append(4)
	if b == 'X':
		n.append(5)
	return n
