from BloqueCache import BloqueCache

class SetCache:
    def __init__(self):
        self.lastUsed = 0
        self.bloque0 = BloqueCache(0)
        self.bloque1 = BloqueCache(1)

    def s_write(self,direccionMemoria, valor):
        if (self.lastUsed == 0):
            self.bloque0.b_direccionSet(direccionMemoria)
            self.bloque0.b_datoSet(valor)
            self.lastUsed = 1
        else:
            self.bloque1.b_direccionSet(direccionMemoria)
            self.bloque1.b_datoSet(valor)
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
            self.bloque0.b_estadoSet = nuevoEstado
            return
        elif (direccionMemoria == self.bloque1.b_direccionGet()):
            self.bloque1.b_estadoSet = nuevoEstado
            return