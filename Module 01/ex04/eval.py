class Evaluator:
	@staticmethod
	def zip_evaluate(coefs,words):
		if len(words) != len(coefs):
			raise Exception("pls give two list of the same length.")
		s = 0
		for i,j in zip(words,coefs):
			s += len(i) * j
		print(s)
	@staticmethod
	def enumerate_evaluate(coefs,words):
		if len(words) != len(coefs):
			print(-1)
			return -1
		s = 0
		for i, j in enumerate(words):
			s += len(j) * coefs[i]
		print(s)

# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
# # Evaluator.zip_evaluate(coefs, words)

# # words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
# # coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
# Evaluator.enumerate_evaluate(coefs, words)