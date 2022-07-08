#!/usr/local/bin/python3

from threading import Lock, Thread

class BuyTicket:
    def __init__(self, availSeats):
        self.availableSeats = availSeats
        self.lock = Lock()

    def purchaseTicket(self, seatsRequested):
        print("Seats Available: ", self.availableSeats)
        # Lock the resource, prevent other threads from changing the data while in use
        self.lock.acquire()
        if self.availableSeats >= seatsRequested:
            print("Confirming seats...")
            print("Processing payment...")
            print("Printing tickets.\n")
            self.availableSeats -= seatsRequested
        else:
            print("Seats not available.")
        # Release the lock on the resource to make it available to other threads again
        self.lock.release()


tickets = BuyTicket(10)

user1 = Thread(target=tickets.purchaseTicket, args=(2, ))
user2 = Thread(target=tickets.purchaseTicket, args=(4, ))
user3 = Thread(target=tickets.purchaseTicket, args=(5, ))

user1.start()
user2.start()
user3.start()
