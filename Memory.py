import time

class Memory:
    def __init__(self, timer):
        self.mem = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
        self.timer = timer

    def memGet(self,position):
        self.sleep()
        return self.mem[position]

    def memSet(self,position,value):
        self.sleep()
        self.mem[position] = value
        return

    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return
    
    def printMemory(self):
        return self.mem