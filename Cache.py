from SetCache import SetCache

class Cache:
    def __init__(self, memory):
        self.memory = memory
        self.set0 = SetCache(self.memory)
        self.set1 = SetCache(self.memory)

    def write(self, direccionMemoria, valor):
        if (direccionMemoria[-1] == '0'):
            return self.set0.s_write(direccionMemoria,valor)
        else:
            return self.set1.s_write(direccionMemoria,valor)

    def read(self, direccionMemoria):
        if (direccionMemoria[-1] == '0'):
            return self.set0.s_read(direccionMemoria)
        else:
            return self.set1.s_read(direccionMemoria)

    def estadoGet(self, direccionMemoria):
        if (direccionMemoria[-1] == '0'):
            return self.set0.s_estadoGet(direccionMemoria)
        else:
            return self.set1.s_estadoGet(direccionMemoria)

    def estadoSet(self, direccionMemoria, nuevoEstado):
        if (direccionMemoria[-1] == '0'):
            return self.set0.s_estadoSet(direccionMemoria,nuevoEstado)
        else:
            return self.set1.s_estadoSet(direccionMemoria,nuevoEstado)
    
    def printCacheValor(self):
        temp = []
        temp.append(self.set0.s_printCacheValor())
        temp.append(self.set0.s_printCacheValor())
        return temp

    def printCacheEstado(self):
        temp = []
        temp.append(self.set0.s_printCacheEstado())
        temp.append(self.set0.s_printCacheEstado())
        return temp

    def printCacheDireccion(self):
        temp = []
        temp.append(self.set0.s_printCacheDireccion())
        temp.append(self.set0.s_printCacheDireccion())
        return temp
