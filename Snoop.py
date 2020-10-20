class Subscriber:
    def __init__(self, processor):
        self.processor = processor
        self.processorList = []
        self.memory = processor.memory
        self.identifier = processor.identifier

    def update(self,senderId,message):
        moesi(self.processorList[senderId],self.processor,self.memory,message)
        return

    def moesi(senderProcessor,processor, memory, message):
        
        return


class Publisher:
    def __init__(self,identifier):
        self.identifier = identifier
        self.subscriber = []

    def register(self,subscriberName):
        self.subscriber.append(subscriberName)
    
    def broadcast(self, senderId, message):
        for subscriber in self.subscriber:
            subscriber.update(senderId,message)

