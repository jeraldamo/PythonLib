# -*- coding: utf-8 -*-
from Jeraldamo.testsuite import *

def returnFalse():
	return False

@test	
def foo():
	assertTrue(True)
	assertEqual(1, 1)
	
@test
def bar():
	assertFalse(returnFalse())
	assertTrue(True)
	
@test
def baz():
	a = 2
	b = 2
	c = 3
	
	assertEqual(a, b)
	assertNotEqual(a, c)
	assertEqualReference(a, b)
	assertNotEqualReference(b, c)
