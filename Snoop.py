class Subscriber:
    def __init__(self, processor):
        self.processor = processor
        self.processorList = []
        self.memory = processor.memory
        self.identifier = processor.identifier

    def update(self,senderId,message, direccionMemoria):
        self.moesi(self.processorList[senderId], self.processor, self.memory, message, direccionMemoria)
        return

    def moesi(self, senderProcessor, processor, memory, message, direccionMemoria):
        if (message == "read miss"):
            if(processor.estadoCacheGet(direccionMemoria) == "E"):
                senderProcessor.Cache.writeX(direccionMemoria, processor.readCache(direccionMemoria))
                senderProcessor.estadoCacheSet(direccionMemoria,"S")
                processor.estadoCacheSet(direccionMemoria,"S")
                return
            
            elif(processor.estadoCacheGet(direccionMemoria) == "S"):
                senderProcessor.Cache.writeX(direccionMemoria, processor.readCache(direccionMemoria))
                senderProcessor.estadoCacheSet(direccionMemoria,"S")
                return
            
        
        elif (message == "read hit"):
            if(processor.estadoCacheGet(direccionMemoria) == "M"):
                processor.estadoCacheSet(direccionMemoria,"O")
                return
                
            elif (processor.estadoCacheGet(direccionMemoria) == "O"):
                return

            elif (processor.estadoCacheGet(direccionMemoria) == "E"):
                processor.estadoCacheSet(direccionMemoria,"S")
                return
            
            elif (processor.estadoCacheGet(direccionMemoria) == "S"):
                return
            
            elif (processor.estadoCacheGet(direccionMemoria) == "M"):
                return

        elif (message == "write hit"):
            if(processor.estadoCacheGet(direccionMemoria) == "M"):
                processor.estadoCacheSet(direccionMemoria,"I")
                return
            elif(processor.estadoCacheGet(direccionMemoria) == "O"):
                processor.estadoCacheSet(direccionMemoria,"I")
                return
            elif(processor.estadoCacheGet(direccionMemoria) == "E"):
                processor.estadoCacheSet(direccionMemoria,"I")
                return
            elif(processor.estadoCacheGet(direccionMemoria) == "S"):
                processor.estadoCacheSet(direccionMemoria,"I")
                return

        elif (message == "write miss"):
            if(processor.estadoCacheGet(direccionMemoria) == "M"):
                processor.estadoCacheSet(direccionMemoria,"I")
                return
            elif(processor.estadoCacheGet(direccionMemoria) == "O"):
                processor.estadoCacheSet(direccionMemoria,"I")
                return
            elif(processor.estadoCacheGet(direccionMemoria) == "E"):
                processor.estadoCacheSet(direccionMemoria,"I")
                return
            elif(processor.estadoCacheGet(direccionMemoria) == "S"):
                processor.estadoCacheSet(direccionMemoria,"I")
                return
            
        return


class Publisher:
    def __init__(self,identifier):
        self.identifier = identifier
        self.subscriber = []

    def register(self,subscriberName):
        self.subscriber.append(subscriberName)
    
    def broadcast(self, senderId, message, direccionMemoria):
        for subscriber in self.subscriber:
            subscriber.update(senderId,message,direccionMemoria)

