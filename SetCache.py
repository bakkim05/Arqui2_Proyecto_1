from BloqueCache import BloqueCache

class SetCache:
    def __init__(self, memory):
        self.lastUsed = 0
        self.memory = memory
        self.bloque0 = BloqueCache(0)
        self.bloque1 = BloqueCache(1)

    def s_write(self,direccionMemoria, valor):
        if (self.s_estadoGet(direccionMemoria) == "O" or self.s_estadoGet(direccionMemoria) == "M"):
            self.s_writeToMem(direccionMemoria,self.s_read(direccionMemoria))
            if (self.lastUsed == 0):
                self.bloque0.b_direccionSet(direccionMemoria)
                self.bloque0.b_datoSet(valor)
                self.lastUsed = 1
            else:
                self.bloque1.b_direccionSet(direccionMemoria)
                self.bloque1.b_datoSet(valor)
                self.lastUsed = 0
            return
        else:
            if (self.lastUsed == 0):
                self.bloque0.b_direccionSet(direccionMemoria)
                self.bloque0.b_datoSet(valor)
                self.s_estadoSet(direccionMemoria,"M")
                self.lastUsed = 1
            else:
                self.bloque1.b_direccionSet(direccionMemoria)
                self.bloque1.b_datoSet(valor)
                self.s_estadoSet(direccionMemoria,"M")
                self.lastUsed = 0
            return
    
    def s_read(self, direccionMemoria):
        if (direccionMemoria == self.bloque0.b_direccionGet()):
            return self.bloque0.b_datoGet()
        elif (direccionMemoria == self.bloque1.b_direccionGet()):
            return self.bloque1.b_datoGet()
        else:
            return


#AQUI HAY UN BUG
    def s_estadoGet(self,direccionMemoria):
        if (direccionMemoria == self.bloque0.b_direccionGet()):
            return self.bloque0.b_estadoGet()
        elif (direccionMemoria == self.bloque1.b_direccionGet()):
            return self.bloque1.b_estadoGet()
        else:
            return "I..."
    
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
    
    def s_printCacheValor(self):
        temp = []
        temp.append(self.bloque0.b_datoGet())
        temp.append(self.bloque1.b_datoGet())
        return temp

    def s_printCacheEstado(self):
        temp = []
        temp.append(self.bloque0.b_estadoGet())
        temp.append(self.bloque1.b_estadoGet())
        return temp

    def s_printCacheDireccion(self):
        temp = []
        temp.append(self.bloque0.b_direccionGet())
        temp.append(self.bloque1.b_direccionGet())
        return temp