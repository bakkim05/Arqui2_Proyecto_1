import time
from numpy import array2string
from Cache import Cache

class Processor:
    def __init__(self, identifier, memory, timer):
        self.identifier = identifier
        self.timer = timer
        self.memory = memory
        self.Cache = Cache(self.memory)
        self.Publisher = None
        self.lastInstruction = ""
        self.lastMessage = ""

    def instruction(self, inst, direccionMemoria, valor):
        self.instructionTextBuilder(inst,direccionMemoria,valor)

        if (inst == 1):
            pass
            #instruccion CALC
        elif (inst == 0):
            self.readCache(direccionMemoria)
        else:
            self.writeCache(direccionMemoria,valor)

        self.sleep()
        return
    
    def instructionTextBuilder(self, inst, direccionMemoria, valor):

        if (inst == "READ"):
            self.lastInstruction = self.instructionSelector(inst)+" "+direccionMemoria
            
        elif (inst == "WRITE"):
            self.lastInstruction = self.instructionSelector(inst)+" "+direccionMemoria+" "+valor
            
        else:
            self.lastInstruction = self.instructionSelector(inst)
        return

    def instructionSelector(self, instruccion):
        if (instruccion == 0):
            return "READ"
        elif (instruccion == 1):
            return "CALC"
        else:
            return "WRITE"

    def writeCache(self, direccionMemoria, valor):
        if (self.estadoCacheGet(direccionMemoria) == "I"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "read miss", direccionMemoria)
            self.lastMessage = "read miss"
            self.estadoCacheSet(direccionMemoria,"M")
            return

        elif(self.estadoCacheGet(direccionMemoria) == "S"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            self.lastMessage = "write hit"
            self.estadoCacheSet(direccionMemoria,"M")
            return

        elif(self.estadoCacheGet(direccionMemoria) == "E"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            self.lastMessage = "write hit"
            self.estadoCacheSet(direccionMemoria,"M")
            return

        elif(self.estadoCacheGet(direccionMemoria) == "O"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            self.lastMessage = "write hit"
            self.estadoCacheSet(direccionMemoria,"M")
            return

        elif(self.estadoCacheGet(direccionMemoria) == "M"):
            self.Cache.write(direccionMemoria,valor)
            self.Publisher.broadcast(self.identifier, "write hit", direccionMemoria)
            self.lastMessage = "write hit"
            return
            
        return

    def readCache(self, direccionMemoria):
        #I (Read Miss, Exclusive) E
        if (self.estadoCacheGet(direccionMemoria) == "I"):
            self.Publisher.broadcast(self.identifier, "read miss", direccionMemoria)
            self.lastMessage = "read miss"
            if (self.estadoCacheGet(direccionMemoria) == "I"):
                self.writeCache(direccionMemoria, self.memory.memGet(int(direccionMemoria,2)))
                self.estadoCacheSet(direccionMemoria,"E")
                return
            return

        #S (Read Hit) S
        elif (self.estadoCacheGet(direccionMemoria) == "S"):
            self.Publisher.broadcast(self.identifier, "read hit", direccionMemoria)
            self.lastMessage = "read hit"
            return self.Cache.read(direccionMemoria)

        #O (Read Hit) O
        elif (self.estadoCacheGet(direccionMemoria) == "O"):
            self.Publisher.broadcast(self.identifier, "read hit", direccionMemoria)
            self.lastMessage = "read hit"
            return self.Cache.read(direccionMemoria)


        else:
            return self.Cache.read(direccionMemoria)
            
        # else:
        #     self.estadoCacheSet(direccionMemoria,"E")
        #     self.writeCache(direccionMemoria,self.memory.memGet(int(direccionMemoria,2)))
        return
        
    def estadoCacheGet(self,direccionMemoria):
        return self.Cache.estadoGet(direccionMemoria)
    
    def estadoCacheSet(self,direccionMemoria,nuevoEstado):
        return self.Cache.estadoSet(direccionMemoria,nuevoEstado)

    def sleep(self):
        time.sleep(self.timer)
        return
