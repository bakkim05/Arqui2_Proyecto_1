import time

class Memory:
    def __init__(self, timer):
        self.mem = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.timer = timer

    def memGet(self,position):
        return self.mem[position]

    def memSet(self,position,value):
        self.mem[position] = value
        return

    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return