import time
import random
from numpy import random

class Processor:
    def __init__(self, timer,policy):
        self.timer = timer
        self.cache = [0,0,0,0]
        self.policy = policy
        self.isFull = False


    #Create Instruction
    def instruction(self):
        #1-Read, 2-Write, 3-Calc
        instruction = random.binomial(n=3, p=0.5, size=1)
        if (instruction == 1):
            memoryPos = random.randint(0,3)
            print ("READ "+ self.decimal_to_binary(memoryPos))
            self.readCache(memoryPos)
        elif (instruction == 2):
            memoryPos = random.randint(0,7)
            writeValue = random.randint(0,65534)
            print("WRITE "+self.decimal_to_hexadecimal(writeValue))
            self.writeCache(writeValue)
        else:
            self.sleep()

                    
    #Cache Write
    def writeCache(self, value):
        self.isCacheFull()
        if (self.isFull):
            if self.policy == "fifo":
                self.fifoPolicy(value)
                return
            elif self.policy == "lifo":
                self.lifoPolicy(value)
                return
            elif self.policy == "random":
                self.randomPolicy(value)
                return
            else:
                self.fifoPolicy(value)
                return
        else:
            for i in range(len(self.cache)):
                if (self.cache[i] == 0):
                    self.cache[i] = value
                    return
        return

    #Cache Read
    def readCache(self, position):
        return self.cache[position]

    #Cache Management
    def cacheFlush(self):
        self.cache = [0,0,0,0]
        return

    def isCacheFull(self):
        x = 0
        
        for i in self.cache:
            if i != 0:
                x += 1
                
        if x == 4:
            self.isFull = True
        else:
            self.isFull = False
        return

    #Politicas de Reemplazo
    def fifoPolicy(self, value):
        self.cache.pop()
        self.cache.insert(0,value)
        return

    def lifoPolicy(self, value):
        self.cache.pop(0)
        self.cache.insert(0,value)
        return

    def randomPolicy(self,value):
        self.cache[random.randint(0,3)] = value
        return

    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return

    #Funciones Auxliares para numeros hex, bin y dec
    def binary_to_decimal(self, binary):
        decimal = 0
        binary = list(str(binary))
        binary = binary[::-1]
        power = 0
        for number in binary:
            if number == '1':
                decimal += 2**power
            power += 1
        return decimal

    def decimal_to_binary(self, decimal):
        binary = bin(decimal).replace('0b','')
        return binary

    def hexadecimal_to_decimal(self, hexadecimal):
        decimal = int(hexadecimal,16)
        return decimal

    def decimal_to_hexadecimal(self, decimal):
        hexadecimal = hex(decimal).replace('0x','')
        return hexadecimal
