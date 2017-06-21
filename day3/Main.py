import hello
import sys,pprint
#import package
import package.testpackage1

import math

from package import testpackage2

print package.__file__
print help(math.acos)
testpackage2.say()

package.testpackage1.say()

hello.say()

hello.test()

pprint.pprint(sys.path)

print dir(package)

print package.__doc__


print [n for n in dir(package) if not n.startswith('_')]
