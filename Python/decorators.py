s = "global var"

def func():
	mylocal = 10
	print(locals())
	print(globals())

print(func())