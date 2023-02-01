def ft_filter(function_to_apply, iterable):
	for i in iterable:
		if function_to_apply(i):
			yield i