"""

Doctests:

	
>>> @adaptor		
... class Foo():
... 	functions = {'bazMethod1': 'barMethod1'}
... 	def __init__(self):
... 		pass
...		
>>> class Bar():
... 	def __init__(self):
... 		pass	
... 	
... 	def barMethod1(self):
... 		print "barMethod1"
... 		
>>> class Baz():
... 	def __init__(self):
... 		pass
... 	
... 	def bazMethod1(self):
... 		print "bazMethod1"
... 	
>>> bar1 = Bar()
>>> baz1 = Baz()
>>> bazToBar = Foo(baz1)
>>> bazToBar.barMethod1()
bazMethod1
"""

from utils import *

class AdaptorException(DesignPatternException):
	pass
	
def adaptor(original_class):
	if type(original_class) != type(CompareClass):
		raise DesignPatternException("Decorator not used on a class")
		
	globals()['AdaptorException'] = AdaptorException

	try:
		orig_init = original_class.__init__
	except AttributeError:
		orig_init = default_init
		
	def __init__(self, *args, **kws):
		self.__adapteeInstance = args[0]
		orig_init(self, *args[1:], **kws)
		
		for key, value in original_class.functions.items():
			setattr(self, value, getattr(self.__adapteeInstance, key))
		
	original_class.__init__ = __init__
	
	return original_class

if __name__ == '__main__':
	import doctest
	doctest.testmod()

