def cesar(arg):
	banderas = len(arg)
	if banderas > 3:
		if arg[1] == "-cc":
			if arg[2] == "-c" or arg[2] == "-d":
				if banderas == 4:
					return True
				else:
					if banderas == 6:
						if arg[4] == "-k" or arg[4] == "-l":
							return True
					else:
						if banderas == 8:
							if arg[4] == "-k" and arg[6] == "-l":
								return True
	return False

def vigenere(arg):
	banderas = len(arg)
	if banderas > 5:
		if arg[1] == "-vg" and arg[4] == "-k":
			if arg[2] == "-c" or arg[2] == "-d":
				if banderas == 6:
					return True
				else:
					if banderas == 8:
						if arg[6] == "-l":
							return True
	return False

def adfgvx(arg):
	if len(arg) == 8:
		if arg[1] == "-ad" and arg[4] == "-k" and arg[6] == "-l":
			if arg[2] == "-c" or arg[2] == "-d":
				return True
	return False
