import add
import importlib


importlib.reload(add)


def testAdd(x,y):
    print(x,y,x+y,add.add(x,y),x+y == add.add(x,y))