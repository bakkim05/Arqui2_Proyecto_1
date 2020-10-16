class Memory:
    def __init__(self):
        self.mem = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def memWrite(self, position, value):
        self.mem[position] = value

    def memRead(self, position):
        return self.mem[position]

    #Funciones Auxliares para numeros hex, bin y dec
    def binary_to_decimal(self, binary):
        decimal = int(binary,2)
        return decimal

    def decimal_to_binary(self, decimal):
        binary = bin(decimal).replace('0b','')
        return binary

    def hexadecimal_to_decimal(self, hexadecimal):
        decimal = int(hexadecimal,16)
        return decimal

    def decimal_to_hexadecimal(self, decimal):
        hexadecimal = hex(decimal).replace('0x','')
        return hexadecimal    
