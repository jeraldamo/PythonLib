from Jeraldamo.testsuite import *
from Factory import *

@factory
class Foo():
	def __init__(self, bar):
		pass
		
class Bar():
	def __init__(self):
		self.a = 1
		self.b = 'b'
		self.c = True


@test
def factoryInstantiation():
	foo = Foo(Bar)
	assertEqual(foo.__productInstance.a, 1)

@test
def factorySetValue():
	foo = Foo(Bar)
	foo._set_value('a', 2)
	assertEqual(foo.__productInstance.a, 2)
	foo._set_value('b', 'a')
	assertEqual(foo.__productInstance.b, 'a')
	foo._set_value('c', False)
	assertFalse(foo.__productInstance.c)

@test
def factoryGetProduct():
	foo = Foo(Bar)
	bar1 = foo._get_product()
	assertEqual(bar1.a, 1)
	assertEqual(bar1.b, 'b')
	assertTrue(bar1.c)

	foo._set_value('a', 2)
	foo._set_value('b', 'a')
	foo._set_value('c', False)
	
	bar2 = foo._get_product()
	assertEqual(bar2.a, 2)
	assertEqual(bar2.b, 'a')
	assertFalse(bar2.c)

	assertNotEqual(bar1, bar2)	