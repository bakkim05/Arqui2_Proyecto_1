import time
from Cache import Cache
from Snoop import Snoop

class Processor:
    def __init__(self, identifier, timer):
        self.identifier = identifier
        self.timer = timer
        self.Cache = Cache()
        self.Snoop = Snoop(self.identifier)

    def writeCache(self,direccionMemoria,valor):
        return self.Cache.write(direccionMemoria,valor)

    def readCache(self,direccionMemoria):
        return self.Cache.read(direccionMemoria)
        
    def estadoCache(self,direccionMemoria):
        return self.Cache.estadoGet(direccionMemoria)

    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return
