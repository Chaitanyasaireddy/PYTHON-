def lengthOfLastWord(a):
	l = 0
	x = a.strip()

	for i in range(len(x)):
		if x[i] == " ":
			l = 0
		else:
			l += 1
	return l
if _name_ == "_main_":
	inp = input("enter the string")
	print("The length of last word is",lengthOfLastWord(inp))
