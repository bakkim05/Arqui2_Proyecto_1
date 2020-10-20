import time
from Cache import Cache

class Processor:
    def __init__(self, identifier, memory, timer):
        self.identifier = identifier
        self.timer = timer
        self.memory = memory
        self.Cache = Cache()

    def writeCache(self,direccionMemoria,valor):
        self.sleep()
        self.Cache.write(direccionMemoria,valor)
        return

    def readCache(self,direccionMemoria):
        self.sleep()
        return self.Cache.read(direccionMemoria)
        
    def estadoCache(self,direccionMemoria):
        return self.Cache.estadoGet(direccionMemoria)

    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return
