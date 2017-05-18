
def unique(string):
	string = string.replace(" ", "")

	for x in range( len(string) ):

		for y in range( len(string) ):
			print ("X =", string[x], "Y =", string[y+1])
			if string[x] == string[y+1]:
				return "Not unique"
				# break
		else:
			print ("Unique string!!")



string = "abcdefghijkl mnoAp"

print (unique(string))