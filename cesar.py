import random
class Cesar:
	def __init__(self, arg):
		self.banderas = len(arg)
		self.clave = 3
		self.lenguaje = "es"
		if self.banderas == 6:
			if arg[4] == "-k":
				self.clave = int(arg[5])
			else:
				if arg[4] == "-l":
					self.lenguaje = arg[5]
		if self.banderas == 8:
			self.clave = int(arg[5])
			self.lenguaje = arg[7]
		if arg[2] == "-c":
			cifrar(arg[3], self.clave, self.lenguaje)
		if arg[2] == "-d":
			descifrar(arg[3], self.clave, self.lenguaje)

def cifrar(archivo, clave, lenguaje):
	abc = alfabeto(lenguaje)
	m = mensaje(archivo)
	cifrado = []
	no = []
	for i in m:
		if i in abc:
			pos = abc.index(i)
			cifrado.append(abc[(pos+clave)%len(abc)])
		else:
			if i not in no:
				no.append(i)
	if len(no) > 0:
		print("No se puede encriptar porque le falta caracteres al alfabeto")
		print("Los caracteres que falta son:")
		print(sorted((list(no))))
	else:
		f = open (archivo+".cif", "w", encoding ='ISO-8859-1')
		for i in cifrado:
			f.write(i)
		f.close()
		print("================================================")
		print()
		print("OPERACION TERMINADA CON EXITO!!!")
		print()
		print("================================================")

def descifrar(archivo, clave, lenguaje):
	abc = alfabeto(lenguaje)
	m = mensaje(archivo)
	descifrado = []
	for i in m:
		if i in abc:
			pos = abc.index(i)
			descifrado.append(abc[(pos-clave)%len(abc)])
		else:
			aux = random.randint(0,len(abc)-1)
			descifrado.append(abc[aux])
	f = open (archivo+".dec", "w", encoding ='ISO-8859-1')
	for i in descifrado:
		f.write(i)
	f.close()
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

def alfabeto(lenguaje):
	if lenguaje == "es":
		archivo = open("Alfabetos/es.txt", "r", encoding ='ISO-8859-1')
		texto = archivo.read()
		archivo.close()
		return texto
	if lenguaje == "en":
		archivo = open("Alfabetos/en.txt", "r", encoding ='ISO-8859-1')
		texto = archivo.read()
		archivo.close()
		return texto
	else:
		archivo = open(lenguaje, "r", encoding ='ISO-8859-1')
		texto = archivo.read()
		archivo.close()
		return texto
