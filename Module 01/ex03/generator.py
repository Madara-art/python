from  random import randint

def generator(text, sep=" ", option=None):
	'''
		Splits the text according to sep value and yield the substrings.
		option precise if a action is performed to the substrings before it is yielded.
	'''
	if option not in ['shuffle','unique','ordered',None]:
		raise Exception("option must be 'shuffle','unique' or 'ordered'")
	if not isinstance(text,str):
		raise Exception("only string.")
	out = text.split(sep)
	lst = out
	if option == 'shuffle':
		s = []
		while len(s)<= len(out):
			s.append(randint(0,len(out)-1))
		lst = []
		for l in s:
			lst.append(out[l])
	if option == 'unique':
		lst = []
		[lst.append(word) for word in out if word not in lst]
	if option == 'ordered':
		lst = sorted(out)
	for t in lst:
		yield t

text = "Le Lorem du Ipsum est simplement du faux texte."
for word in generator(text, sep = " ",option='unique'):
	print(word)