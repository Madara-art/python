import math

class TinyStatistician:
	@staticmethod
	def mean(lst):
		if lst:
			return sum(lst)/len(lst)
		return None

	@staticmethod
	def median(lst):
		if lst:
			lst.sort()

			if len(lst) % 2 == 0:
				return float((lst[len(lst)//2] + lst[len(lst)//2 - 1])/2)
			return float(lst[len(lst)//2])

	@staticmethod
	def quartiles(lst):
		if lst:
			lst.sort()
			if len(lst) % 2:
				lst_q1 = lst[:len(lst)//2 + 1]
				lst_q3 = lst[len(lst)//2:]
			else:
				lst_q1 = lst[:len(lst)//2]
				lst_q3 = lst[len(lst)//2:]
			return [TinyStatistician.median(lst_q1),TinyStatistician.median(lst_q3)]
	@staticmethod
	def var(lst):
		if lst:
			return sum([(x - TinyStatistician.mean(lst))**2/len(lst) for x in lst])
	@staticmethod
	def std(lst):
		if lst:
			return math.sqrt(TinyStatistician.var(lst))
# tstat = TinyStatistician()
# a = [1, 2, 3, 10]
# print(tstat.mean(a))
# print(tstat.median(a))
# print(tstat.quartiles(a))

