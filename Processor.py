import time
import random

class Processor:
    def __init__(self, timer,policy):
        self.timer = timer
        self.cache = [0,0,0,0]
        self.policy = policy
        self.isFull = False

    def insertCache(self, value):
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

    def sleep(self, timer):
        time.sleep(timer)
        return

    
