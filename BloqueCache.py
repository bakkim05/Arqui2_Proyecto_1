class BloqueCache:
    def __init__(self, identifier):
        self.identifier = identifier
        self.estado = 'I'  #M=0, O=1, E=2, S=3, I=4
        self.direccion = ''
        self.dato = ''

    #Setter and Getters for Estado
    def b_estadoSet(self,nuevoEstado):
        self.estado = nuevoEstado
        return
    def b_estadoGet(self):
        return self.estado
    
    #Setter and Getters for Direccion
    def b_direccionSet(self,nuevaDireccion):
        self.direccion = nuevaDireccion
        return
    def b_direccionGet(self):
        return self.direccion

    #Setter and Getters for Dato
    def b_datoSet(self,nuevoDato):
        self.dato = nuevoDato
        return
    def b_datoGet(self):
        return self.dato