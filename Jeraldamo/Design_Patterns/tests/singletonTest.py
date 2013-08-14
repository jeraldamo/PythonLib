from Jeraldamo.testsuite import *
from Singleton import *

@singleton
class Foo():
	def __init__(self, value):
		self.value = value
		
	def getValue(self):
		return self.value

@test		
def singletonInstantiation():
	foo1 = Foo(1)
	assertEqual(foo1.getValue(), 1)
	foo1._delete()
	
@test
def singletonDeletion():
	foo1 = Foo(1)
	foo1._delete()
	foo2 = Foo(2)
	assertNotEqual(foo1, foo2)
	foo2._delete()

# @test
# def testExcpetion():
# 	foo1 = Foo(1)
# 	excepetionString = ''
# 	try:
# 		foo2 = Foo(2)
# 	except SingletonException, e:
# 		excepetionString = e

# 	assertEqual(excepetionString, "Class instance already created")