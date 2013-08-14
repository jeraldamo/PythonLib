"""
This module provides a decorator to constrain a 
class with the Singleton design pattern

Doctests:

>>> @singleton
... class Foo():
...     def __init__(self, value):
...			self.value = value
... 	def getValue(self):
... 		return self.value
...
>>> foo1 = Foo(1)
>>> foo1._delete()
>>> foo2 = Foo(2)
>>> try:
... 	foo3 = Foo(3)
... except SingletonException:
... 	Foo._get_cur_instance()._delete()
... 	foo3 = Foo(3)
...
>>> foo3.getValue()
3
>>> try:
... 	@singleton
... 	def Bar():
... 		pass
... except DesignPatternException, e:
... 	print e
...
Decorator not used on a class
"""

from utils import *

class SingletonException(DesignPatternException):
	pass

def singleton(original_class):
	if type(original_class) != type(CompareClass):
		raise DesignPatternException("Decorator not used on a class")
		
	globals()['SingletonException'] = SingletonException

	try:
		orig_init = original_class.__init__
	except AttributeError:
		orig_init = default_init
	
	def __init__(self, *args, **kws):
		orig_init(self, *args, **kws)
		original_class.__cur_instance = self
		original_class.__init__ = __raiseSingletonException
		
	def __del__(self):
		original_class.__init__ = __init__
		original_class.__cur_instance = None
		del self

	def __raiseSingletonException(self, *args, **kws):
		raise SingletonException("Class instance already created")

	def _delete(self):
		__del__(self)

	@staticmethod
	def _get_cur_instance():
		return original_class.__cur_instance

	original_class.__init__ = __init__
	original_class._delete = _delete
	original_class._get_cur_instance = _get_cur_instance
	
	return original_class

def default_init(self):
	pass

if __name__ == '__main__':
	import doctest
	doctest.testmod()
