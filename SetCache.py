from BloqueCache import BloqueCache

class SetCache:
    def __init__(self, memory):
        self.lastUsed = 0
        self.memory = memory
        self.bloque0 = BloqueCache(0)
        self.bloque1 = BloqueCache(1)

    def s_write(self,direccionMemoria, valor):
        if (self.lastUsed == 0):
            if (self.bloque0.b_direccionGet() == direccionMemoria):
                self.bloque0.b_datoSet(valor)
                self.bloque0.b_estadoSet("M")
                return

            else:
                if (self.bloque0.b_estadoGet() == "M"):
                    self.memory.memSet(int(self.bloque0.b_direccionGet(),2),self.bloque0.b_datoGet())
                    self.bloque0.b_direccionSet(direccionMemoria)
                    self.bloque0.b_datoSet(valor)
                    
                elif (self.bloque0.b_estadoGet() == "O"):
                    self.memory.memSet(int(self.bloque0.b_direccionGet(),2),self.bloque0.b_datoGet())
                    self.bloque0.b_direccionSet(direccionMemoria)
                    self.bloque0.b_datoSet(valor)
                    self.bloque0.b_estadoSet("M")
                
                elif (self.bloque0.b_estadoGet() == "E"):
                    self.memory.memSet(int(self.bloque0.b_direccionGet(),2),self.bloque0.b_datoGet())
                    self.bloque0.b_direccionSet(direccionMemoria)
                    self.bloque0.b_datoSet(valor)
                    self.bloque0.b_estadoSet("M")                
                
                else:
                    self.bloque0.b_direccionSet(direccionMemoria)
                    self.bloque0.b_datoSet(valor)
                    self.bloque0.b_estadoSet("M")
                    
                self.lastUsed = 1
                return
                
        else:
            if (self.bloque1.b_direccionGet() == direccionMemoria):
                self.bloque1.b_datoSet(valor)
                self.bloque1.b_estadoSet("M")
                return

            else:
                if (self.bloque1.b_estadoGet() == "M"):
                    self.memory.memSet(int(self.bloque1.b_direccionGet(),2),self.bloque1.b_datoGet())
                    self.bloque1.b_direccionSet(direccionMemoria)
                    self.bloque1.b_datoSet(valor)     
                    
                elif (self.bloque1.b_estadoGet() == "O"):
                    self.memory.memSet(int(self.bloque1.b_direccionGet(),2),self.bloque1.b_datoGet())
                    self.bloque1.b_direccionSet(direccionMemoria)
                    self.bloque1.b_datoSet(valor)
                    self.bloque1.b_estadoSet("M")
                
                elif (self.bloque1.b_estadoGet() == "E"):
                    self.memory.memSet(int(self.bloque1.b_direccionGet(),2),self.bloque1.b_datoGet())
                    self.bloque1.b_direccionSet(direccionMemoria)
                    self.bloque1.b_datoSet(valor)
                    self.bloque1.b_estadoSet("M")
                
                else:
                    self.bloque1.b_direccionSet(direccionMemoria)
                    self.bloque1.b_datoSet(valor)
                    self.bloque1.b_estadoSet("M")

                self.lastUsed = 0
                return

    
    def s_read(self, direccionMemoria):
        if (direccionMemoria == self.bloque0.b_direccionGet()):
            return self.bloque0.b_datoGet()
        elif (direccionMemoria == self.bloque1.b_direccionGet()):
            return self.bloque1.b_datoGet()
        else:
            return

    def s_estadoGet(self,direccionMemoria):
        if (direccionMemoria == self.bloque0.b_direccionGet()):
            return self.bloque0.b_estadoGet()
        elif (direccionMemoria == self.bloque1.b_direccionGet()):
            return self.bloque1.b_estadoGet()
        else:
            return "I" 
    
    def s_estadoSet(self,direccionMemoria, nuevoEstado):
        if (direccionMemoria == self.bloque0.b_direccionGet()):
            self.bloque0.b_estadoSet(nuevoEstado)
            return
        elif (direccionMemoria == self.bloque1.b_direccionGet()):
            self.bloque1.b_estadoSet(nuevoEstado)
            return

    def s_writeToMem(self, memory, direccionMemoria, valor):
        self.memory.memSet(int(direccionMemoria,2),valor)
        return