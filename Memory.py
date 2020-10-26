import time
from threading import Lock

class Memory:
    def __init__(self, timer):
        self.mem = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
        self.timer = timer
        self.mutex = Lock()

    def memGet(self,position):
        self.mutex.acquire()
        self.sleep()
        self.mutex.release()
        return self.mem[position]

    def memSet(self,position,value):
        self.mutex.acquire()
        self.sleep()
        self.mem[position] = value
        self.mutex.release()
        return

    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return
    
    def printMemory(self):
        return self.mem