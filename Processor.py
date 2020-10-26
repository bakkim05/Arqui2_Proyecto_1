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
        self.previousInstruction = ""
        self.instructionPrint = ""
        self.lastMessage = ""

    def instruction(self, inst, direccionMemoria, valor):
        self.previousInstruction = self.lastInstruction
        self.lastInstruction = ""

        if (inst == 0):
            self.lastInstruction = self.instructionSelector(inst)+" "+direccionMemoria
            self.readCache(direccionMemoria)
            
        elif (inst == 2):
            self.lastInstruction = self.instructionSelector(inst)+" "+direccionMemoria+" "+valor
            self.writeCache(direccionMemoria,valor)
            
        else:
            self.lastInstruction = self.instructionSelector(inst)
            self.lastMessage = ""
            pass

        self.instructionPrint = self.previousInstruction + " || " + self.lastInstruction

        return

    def instructionSelector(self, instruccion):
        if (instruccion == 0):
            return "READ"
        elif (instruccion == 1):
            return "CALC"
        else:
            return "WRITE"

#-------Cache Related Operations-----------------
    def writeCache(self, direccionMemoria, valor):
        if (self.estadoCacheGet(direccionMemoria) == "I"):
            self.Cache.write(direccionMemoria,valor)
            self.lastMessage = "write miss"
            self.Publisher.broadcast(self.identifier, "write miss", direccionMemoria)
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
                self.lastMessage = "read miss"
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

        return
        
    def estadoCacheGet(self,direccionMemoria):
        return self.Cache.estadoGet(direccionMemoria)
    
    def estadoCacheSet(self,direccionMemoria,nuevoEstado):
        return self.Cache.estadoSet(direccionMemoria,nuevoEstado)
#-------------------------------------------------

    def sleep(self):
        time.sleep(self.timer)
        return
