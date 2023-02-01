def ft_reduce(function_to_apply, iterable):
	s = iterable[0]
	for i in iterable[1:]:
		s = function_to_apply(s,i)
	return s