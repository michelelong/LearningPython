#!/usr/local/bin/python3

from threading import Thread, current_thread

# Threading 3 ways
# 1) Instantiate Thread class with a function as an arugment
# 2) Instantiate a subclass inheriting from the Thread class
# 3) Instantiate a class and a Thread with the class method as an argument

current_thread().setName("***Main Python Thread***")
print(current_thread().getName())

def displayNumbers():
    i = 0
    current_thread().setName("Thread with function arugment")
    nameMain = current_thread().getName()
    while i <= 10:
        print(nameMain, ": ", i)
        i += 1


t = Thread(target=displayNumbers)
t.start()


class ThreadAsAClass(Thread):
    # Override the run method inherited from the Thread superclass
    def run(self):
        i = 0
        current_thread().setName("Threaded Subclass")
        nameClass = current_thread().getName()
        while i <= 10:
            print(nameClass, ": ", i)
            i += 1


tc = ThreadAsAClass()
tc.start()


class ThreadAsAMethod():
    def displayNumbers(self):
        i = 0
        current_thread().setName("Threaded Method")
        nameMethod = current_thread().getName()
        while i <= 10:
            print(nameMethod, ": ", i)
            i += 1


tm = ThreadAsAMethod()
tmThread = Thread(target=tm.displayNumbers)
tmThread.start()

print(current_thread().getName())
