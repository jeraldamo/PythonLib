"""

Doctests:

>>> @factory
... class Foo():
... 	def __init__(self, bar):
... 		pass
... 		
>>> class Bar():
... 	def __init__(self):
... 		self.a = 1
... 		self.b = 'b'
... 		self.c = True
... 		
>>> foo1 = Foo(Bar)
>>> print foo1.__productInstance.a
1
>>> print foo1._set_value('a', 2)
2
>>> print foo1.__productInstance.a
2
>>> print foo1._set_value('b', 'a')
a
>>> print foo1._set_value('d', False)
False
>>> bar1 = foo1._get_product()
>>> print bar1.a, bar1.b, bar1.c, bar1.d
2 a True False
>>> bar2 = foo1._get_product()
>>> print bar2.a, bar2.b, bar2.c
1 b True
>>> try:
... 	@factory
... 	def Bar():
... 		pass
... except DesignPatternException, e:
... 	print e
...
Decorator not used on a class
"""

from utils import *

class FactoryException(DesignPatternException):
	pass

def factory(original_class):
	if type(original_class) != type(CompareClass):
		raise DesignPatternException("Decorator not used on a class")
	
	globals()['FactoryException'] = FactoryException
		
	try:
		orig_init = original_class.__init__
	except AttributeError:
		orig_init = default_init
	
	def __init__(self, *args, **kws):
		self.__productClass = args[0]
		self.__productInstance = self.__productClass()
		
		orig_init(self, *args, **kws)
		
		
	def _set_value(self, variable, newValue = None):
		if newValue != None:
			setattr(self.__productInstance, variable, newValue)
			
		return getattr(self.__productInstance, variable)
					
	def _get_product(self):
		tmp = self.__productInstance
		self.__productInstance = self.__productClass()
		return tmp

	original_class.__init__ = __init__
	original_class._get_product = _get_product
	original_class._set_value = _set_value
	
	return original_class

if __name__ == '__main__':
	import doctest
	doctest.testmod()

