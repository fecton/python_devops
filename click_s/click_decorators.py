def some_decorator(wrapped_function):
	def wrapper():
		print("Do something before calling wrapped function")
		wrapped_function()
		print("Do something after calling wrapped function")
	return wrapper

def footbat():
	print('footbat')

f = some_decorator(footbat)
f()

@some_decorator
def batfoo():
	print('batfoo')
batfoo()


