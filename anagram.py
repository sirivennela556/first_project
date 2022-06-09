D1={}
D2={}

def anagrams(s1,s2):
	if len(s1)!=len(s2):
		return False
	else:
		elementNumber = 0
		for char in s1:      #Load s1 into dictionary
			D1[elementNumber] = char
			elementNumber = elementNumber + 1
		elementNumber = 0
		for char in s2:	     #Load s2 into disctionary
			D2[elementNumber] = char
			elementNumber = elementNumber + 1
		print(sorted(D1.values()))      #Example output
		print(sorted(D2.values()))	#example output
		if sorted(D1.values())==sorted(D2.values()):          #Sort and compare
			return True
		else:
			return False
print("Anagrams: "+str(anagrams("Hello", "oHlel")))      #Return True
print("Anagrams: "+str(anagrams("Hello", "xyzlo")))      #Return False
