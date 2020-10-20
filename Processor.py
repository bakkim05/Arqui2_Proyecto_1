import time
from Cache import Cache

class Processor:
    def __init__(self, identifier, memory, timer):
        self.identifier = identifier
        self.timer = timer
        self.memory = memory
        self.Cache = Cache(self.memory)
        self.Publisher = None

    def instruction(self, inst, direccionMemoria, valor):
        if (inst == 1):
            pass
            #instruccion CALC
        elif (inst == 0):
            self.readValidator(direccionMemoria)
        else:
            self.writeValidator(direccionMemoria,valor)

        self.sleep()
        return

    def writeCache(self,direccionMemoria,valor):
        self.Cache.write(direccionMemoria,valor)
        return

    def readCache(self,direccionMemoria):
        return self.Cache.read(direccionMemoria)

    def writeValidator(self, direccionMemoria, valor):
        if (self.estadoCacheGet(direccionMemoria) == "I"):
            self.writeCache(direccionMemoria,valor)
            self.estadoCacheSet(direccionMemoria,"M")
            self.Publisher.broadcast(self.identifier, "write miss", direccionMemoria)
        elif(self.estadoCacheGet(direccionMemoria) == "S"):
            self.writeCache(direccionMemoria,valor)
            self.estadoCacheSet(direccionMemoria,"M")
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            return

        elif(self.estadoCacheGet(direccionMemoria) == "E"):
            self.writeCache(direccionMemoria,valor)
            self.estadoCacheSet(direccionMemoria,"M")
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            return

        elif(self.estadoCacheGet(direccionMemoria) == "O"):
            self.writeCache(direccionMemoria,valor)
            self.estadoCacheSet(direccionMemoria,"M")
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            return

        elif(self.estadoCacheGet(direccionMemoria) == "M"):
            self.writeCache(direccionMemoria,valor)
            return
            
        return

    def readValidator(self, direccionMemoria):
        if (self.estadoCacheGet(direccionMemoria) == "I"):
            self.Publisher.broadcast(self.identifier, "read miss", direccionMemoria)
            if (self.estadoCacheGet(direccionMemoria) == "I"):
                self.writeCache(direccionMemoria, self.memory.memGet(int(direccionMemoria,2)))
                self.estadoCacheSet(direccionMemoria,"E")
                return
            return
        elif (self.estadoCacheGet(direccionMemoria) == "S"):
            self.readCache(direccionMemoria)
            return
        elif (self.estadoCacheGet(direccionMemoria) == "E"):
            self.readCache(direccionMemoria)
            return
        elif (self.estadoCacheGet(direccionMemoria) == "O"):
            self.readCache(direccionMemoria)
            return
        elif (self.estadoCacheGet(direccionMemoria) == "M"):
            self.readCache(direccionMemoria)
            return
        else:
            self.estadoCacheSet(direccionMemoria,"E")
            self.writeCache(direccionMemoria,self.memory.memGet(int(direccionMemoria,2)))
        return
        
    def estadoCacheGet(self,direccionMemoria):
        return self.Cache.estadoGet(direccionMemoria)
    
    def estadoCacheSet(self,direccionMemoria,nuevoEstado):
        return self.Cache.estadoSet(direccionMemoria,nuevoEstado)

    def printCacheValue(self):
        return self.Cache.printCacheValor()

    def printCacheEstado(self):
        return self.Cache.printCacheEstado()

    def printCacheDireccion(self):  
        return self.Cache.printCacheDireccion()
    
    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return
