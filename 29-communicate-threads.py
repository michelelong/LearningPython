#!/usr/local/bin/python3

from time import sleep
from threading import Condition, Thread

class Producer:
    def __init__(self):
        self.products = []
        # Condition object notifiies waiting threads of status
        self.status = Condition()

    def produceOrder(self):
        self.status.acquire()
        for i in range(1, 5):
            self.products.append("Product #" + str(i))
            sleep(1)
            print("Product added.")
        self.status.notify()
        self.status.release()


class Consumer:
    def __init__(self, order):
        self.order = order

    def consumeOrder(self):
        # Lock and wait for notification
        self.order.status.acquire()
        self.order.status.wait(timeout=0)
        print("Order Processed: ", self.order.products)
        self.order.status.release()


prod = Producer()
cons = Consumer(prod)

t1 = Thread(target=prod.produceOrder)
t2 = Thread(target=cons.consumeOrder)
t1.start()
t2.start()
