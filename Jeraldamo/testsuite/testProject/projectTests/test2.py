# -*- coding: utf-8 -*-
from Jeraldamo.testsuite import *
import squareRoot

@test
def otherTest():
	assertLessThan(4, 7)
	
@test
def testSqrt():
	assertEqual(squareRoot.sqrt(4), 2)
