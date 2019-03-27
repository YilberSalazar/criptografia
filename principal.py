import sys
from time import time
#Importar las clases de cifrado
from cesar import Cesar
from vigenere import Vigenere
from adfgvx import Adfgvx
import valido
import menu
def main():
	if len(sys.argv) < 2:
		menu.algoritmos()
		exit()
	if sys.argv[1] == "-cc":
		if valido.cesar(sys.argv) == False:
			menu.cesar()
		else:
			if sys.argv[2] == "-c" or sys.argv[2] == "-d":
				ti = time()
				Cesar(sys.argv)
				tf = time()
				te = tf - ti
				print("El tiempo de ejecucion fue: ", te)
				menu.mensaje()
	if sys.argv[1] == "-vg":
		if valido.vigenere(sys.argv) == False:
			menu.vigenere()
		else:
			if sys.argv[2] == "-c" or sys.argv[2] == "-d":
				ti = time()
				Vigenere(sys.argv)
				tf = time()
				te = tf - ti
				print("El tiempo de ejecucion fue: ", te)
				menu.mensaje()
	if sys.argv[1] == "-ad":
		if valido.adfgvx(sys.argv) == False:
			menu.adfgvx()
		else:
			if sys.argv[2] == "-c" or sys.argv[2] == "-d":
				ti = time()
				Adfgvx(sys.argv)
				tf = time()
				te = tf - ti
				print("El tiempo de ejecucion fue: ", te)
				menu.mensaje()

if __name__ == '__main__':
    main()
