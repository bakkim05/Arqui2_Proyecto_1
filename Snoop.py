class Snoop:
    def __init__(self,identifier):
        self.identifier = identifier
        self.message = ""

    def messageSet(self,message):
        self.message = message
        return
    
    def messageGet(self):
        return self.message