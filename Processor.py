import time
from Cache import Cache

class Processor:
    def __init__(self, timer):
        self.timer = timer
        self.Cache = Cache()

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
