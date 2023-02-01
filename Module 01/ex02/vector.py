class Vector:
	def __init__(self, values):
		self.values = values
		self.shape = (len(self.values),len(self.values[0]))

	def T(self):
		if self.shape[1]==1:
			self.values = [[x] for x in [y for i in self.values for y in i]]
		else:
			self.values = [[x for x in [y for i in self.values for y in i]]]
		return self

	def dot(self,v2):
		if self.shape != v2.shape:
			raise Exception("shapes need to be equal.")
		if self.shape[1]==1:
			res = [[x * x1] for (x,x1) in zip([y for i in self.values for y in i], [y1 for i1 in v2.values for y1 in i1])]
		else:
			res = [[x * x1 for x,x1 in zip([y for i in self.values for y in i], [y1 for i1 in v2.values for y1 in i1])]]
		return sum([x for i in res for x in i])

	def __add__(self,other):
		if self.shape == other.shape:
			if self.shape[1]==1:
				res = [[x + x1] for (x,x1) in zip([y for i in self.values for y in i], [y1 for i1 in other.values for y1 in i1])]
			else:
				res = [[x + x1 for x,x1 in zip([y for i in self.values for y in i], [y1 for i1 in other.values for y1 in i1])]]
			return Vector(res)
		else:
			raise Exception("Vectors need to have the same shape.")

	def __radd__(self,other):
		if self.shape == other.shape:
			if self.shape[1]==1:
				res = [[x + x1] for (x,x1) in zip([y for i in self.values for y in i], [y1 for i1 in other.values for y1 in i1])]
			else:
				res = [[x+x1 for x,x1 in zip([y for i in self.values for y in i], [y1 for i1 in other.values for y1 in i1])]]
			return Vector(res)
		else:
			raise Exception("Vectors need to have the same shape.")

	def __truediv__(self,other):
		if not isinstance(other,float) and not isinstance(other,int):
			raise Exception("can't devide by a non int/float.")
		if other == 0:
			raise ZeroDivisionError("division by zero.")
		if self.shape[1]==1:
			res = [[x / other] for x in [y for i in self.values for y in i]]
		else:
			res = [[x / other for x in [y for i in self.values for y in i]]]
		return Vector(res)

	def __rtruediv__(self):
		raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

	def __mul__(self,other):
		if not isinstance(other,float) and not isinstance(other,int):
			raise Exception("can't multiply by a non int/float.")
		if self.shape[1]==1:
			res = [[x * other] for x in [y for i in self.values for y in i]]
		else:
			res = [[x * other for x in [y for i in self.values for y in i]]]
		return Vector(res)

	def __rmul__(self,other):
		if not isinstance(other,float) and not isinstance(other,int):
			raise Exception("can't multiply by a non int/float.")
		if self.shape[1]==1:
			res = [[x * other] for x in [y for i in self.values for y in i]]
		else:
			res = [[x * other for x in [y for i in self.values for y in i]]]
		return Vector(res)

	def __sub__(self,other):
		if self.shape == other.shape:
			if self.shape[1]==1:
				res = [[x - x1] for (x,x1) in zip([y for i in self.values for y in i], [y1 for i1 in other.values for y1 in i1])]
			else:
				res = [[x - x1 for x,x1 in zip([y for i in self.values for y in i], [y1 for i1 in other.values for y1 in i1])]]
			return Vector(res)
		else:
			raise Exception("Vectors need to have the same shape.")

	def __rsub__(self,other):
		if self.shape == other.shape:
			if self.shape[1]==1:
				res = [[x1 - x] for (x,x1) in zip([y for i in self.values for y in i], [y1 for i1 in other.values for y1 in i1])]
			else:
				res = [[x1 - x for x,x1 in zip([y for i in self.values for y in i], [y1 for i1 in other.values for y1 in i1])]]
			return Vector(res)
		else:
			raise Exception("Vectors need to have the same shape.")

	def __str__(self):
		return f"this is a vector object: Vector({self.values})"

	def __repr__(self):
		return f"Vector({self.values})"