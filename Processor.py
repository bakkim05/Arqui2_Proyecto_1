import time
from Cache import Cache

class Processor:
    def __init__(self, identifier, memory, timer):
        self.identifier = identifier
        self.timer = timer
        self.memory = memory
        self.Cache = Cache()
        self.Publisher = None

    def instruction(self, inst, direccionMemoria, valor):
        if (inst == 1):
            self.sleep()
        elif (inst == 0):
            self.readValidator(direccionMemoria)
        else:
            self.writeValidator(direccionMemoria,valor)
        return

    def writeCache(self,direccionMemoria,valor):
        self.sleep()
        self.Cache.write(direccionMemoria,valor)
        return

    def readCache(self,direccionMemoria):
        self.sleep()
        return self.Cache.read(direccionMemoria)

    def writeValidator(self, direccionMemoria, valor):
        return

    def readValidator(self, direccionMemoria):
        return
        
    def estadoCache(self,direccionMemoria):
        return self.Cache.estadoGet(direccionMemoria)

    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return
