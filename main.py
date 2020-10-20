from Processor import Processor
from Memory import Memory
from Snoop import Subscriber, Publisher
import threading
import time
import numpy as np

def subscribeToPublisher(publisher, subscribers):
    publisher[0].register(subscribers[1])
    publisher[0].register(subscribers[2])
    publisher[0].register(subscribers[3])
    

    publisher[1].register(subscribers[0])
    publisher[1].register(subscribers[2])
    publisher[1].register(subscribers[3])

    publisher[2].register(subscribers[0])
    publisher[2].register(subscribers[1])
    publisher[2].register(subscribers[3])

    publisher[3].register(subscribers[0])
    publisher[3].register(subscribers[1])
    publisher[3].register(subscribers[2])


def processorToSubscriber(processor, subscribers):
    subscriber[0].processorList = processor
    subscriber[1].processorList = processor
    subscriber[2].processorList = processor
    subscriber[3].processorList = processor



if __name__ == "__main__":

    processor = []
    subscriber = []
    publisher = []

    memory = Memory(2)
    for i in range(4):
        processor.append(Processor(i,memory,1))
        subscriber.append(Subscriber(processor[i]))
        publisher.append(Publisher(i))

    subscribeToPublisher(publisher,subscriber)
    processorToSubscriber(processor,publisher)


    publisher[3].broadcast("hello world")

