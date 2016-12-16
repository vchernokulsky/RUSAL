import threading
import time
import random


class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args)

"""
# Example usage
def someOtherFunc(data, key):
    i = 0
    while i<10:
        print "someOtherFunc was called : data=%s; key=%s" % (str(data), str(key))
        time.sleep(3)
        step = random.uniform(0, 1)
        print 'OK ', step
        i+=1

t1 = FuncThread(someOtherFunc, [1, 2], 6)
t1.start()
t1.join()
"""