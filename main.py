from Processor import Processor
from Memory import Memory
from Snoop import Subscriber, Publisher
from numpy import random
import threading
import time

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
    return

def processorToSubscriber(processor, subscribers):
    for i in range(4):
        subscriber[i].processorList = processor
    return

def publisherToProcessor(processor, publisher):

    for i in range(4):
        processor[i].Publisher = publisher[i]
    return

def generatorSingle(processor):
    [numProcesador, instruccion, direccionMemoria, valor] = generatorInstruction()
    p = processor[numProcesador]
    
    if (instruccion == 1):
        print("P"+str(numProcesador)+": CALC")
    elif (instruccion == 0):
        print("P"+str(numProcesador)+": READ " + direccionMemoria)
    else:
        print("P"+str(numProcesador)+": Write " + direccionMemoria+';'+valor)

    #p.instruccion(instruccion, direccionMemoria, valor)
    return

def generatorContinous():
    while(True):
        return
    return

def generatorIteraciones(processor, memory, iteraciones):
    for i in range(iteraciones):
        [numProcesador, instruccion, direccionMemoria, valor] = generatorInstruction()
        p = processor[numProcesador]
        
        if (instruccion == 1):
            print("P"+str(numProcesador)+": CALC")
        elif (instruccion == 0):
            print("P"+str(numProcesador)+": READ " + direccionMemoria)
        else:
            print("P"+str(numProcesador)+": WRITE " + direccionMemoria+';'+valor)
        p.instruction(instruccion, direccionMemoria, valor)
        printMemoryAndCache(processor,memory)
    return

def generatorInstruction():
    numProcesador = random.randint(0,3)
    instruccion = random.binomial(n=2,p=0.5,size=1)[0]
    direccionMemoria = bin(random.randint(0,15)).replace('0b','')
    valor = hex(random.randint(0,65535)).replace('0x','')
    
    return [numProcesador,instruccion,direccionMemoria,valor]


def printMemoryAndCache(processor,memory):
    for i in range(4):
        print('------------------P'+str(i)+'------------------')
        print(processor[i].printCacheValue())
        print(processor[i].printCacheEstado())
        print(processor[i].printCacheDireccion())
        print('--------------------------------------')
    print(memory.printMemory())

if __name__ == "__main__":

    processor = []
    subscriber = []
    publisher = []

    #Initialize Processor, Subscriber, Publisher, and Memory
    memory = Memory(2)
    for i in range(4):
        processor.append(Processor(i,memory,1))
        subscriber.append(Subscriber(processor[i]))
        publisher.append(Publisher(i))

    #Add Subscribers to Publishers
    subscribeToPublisher(publisher,subscriber)

    #Add processors to the Subscriber
    processorToSubscriber(processor,subscriber)

    #Add publishers to processors
    publisherToProcessor(processor,publisher)

    generatorIteraciones(processor, memory, 2)
