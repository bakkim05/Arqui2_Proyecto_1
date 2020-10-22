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
            self.readCache(direccionMemoria)
        else:
            self.writeCache(direccionMemoria,valor)

        self.sleep()
        return

    def writeCache(self, direccionMemoria, valor):
        if (self.estadoCacheGet(direccionMemoria) == "I"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "write miss", direccionMemoria)
            return

        elif(self.estadoCacheGet(direccionMemoria) == "S"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            return

        elif(self.estadoCacheGet(direccionMemoria) == "E"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            return

        elif(self.estadoCacheGet(direccionMemoria) == "O"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            return

        elif(self.estadoCacheGet(direccionMemoria) == "M"):
            self.Cache.write(direccionMemoria,valor)
            return
            
        return

    #REVISAR
    def readCache(self, direccionMemoria):
        if (self.estadoCacheGet(direccionMemoria) == "I"):
            self.Publisher.broadcast(self.identifier, "read miss", direccionMemoria)
            if (self.estadoCacheGet(direccionMemoria) == "I"):
                self.writeCache(direccionMemoria, self.memory.memGet(int(direccionMemoria,2)))
                self.estadoCacheSet(direccionMemoria,"E")
                return
            return
        elif (self.estadoCacheGet(direccionMemoria) == "S"):
            return self.Cache.read(direccionMemoria)
        elif (self.estadoCacheGet(direccionMemoria) == "E"):
            return self.Cache.read(direccionMemoria)
        elif (self.estadoCacheGet(direccionMemoria) == "O"):
            return self.Cache.read(direccionMemoria)
        elif (self.estadoCacheGet(direccionMemoria) == "M"):
            return self.Cache.read(direccionMemoria)
        else:
            self.estadoCacheSet(direccionMemoria,"E")
            self.writeCache(direccionMemoria,self.memory.memGet(int(direccionMemoria,2)))
        return
        
    def estadoCacheGet(self,direccionMemoria):
        return self.Cache.estadoGet(direccionMemoria)
    
    def estadoCacheSet(self,direccionMemoria,nuevoEstado):
        return self.Cache.estadoSet(direccionMemoria,nuevoEstado)

    def printCacheValue(self):
        temp = []
        temp.append(self.Cache.set0.bloque0.dato)
        temp.append(self.Cache.set0.bloque1.dato)
        temp.append(self.Cache.set1.bloque0.dato)
        temp.append(self.Cache.set1.bloque1.dato)
        return temp

    def printCacheEstado(self):
        temp = []
        temp.append(self.Cache.set0.bloque0.estado)
        temp.append(self.Cache.set0.bloque1.estado)
        temp.append(self.Cache.set1.bloque0.estado)
        temp.append(self.Cache.set1.bloque1.estado)
        return temp

    def printCacheDireccion(self):
        temp = [] 
        temp.append(self.Cache.set0.bloque0.direccion)
        temp.append(self.Cache.set0.bloque1.direccion)
        temp.append(self.Cache.set1.bloque0.direccion)
        temp.append(self.Cache.set1.bloque1.direccion)
        return temp
    
    #Descanso
    def sleep(self):
        time.sleep(self.timer)
        return
