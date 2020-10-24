from tkinter import Tk, Label, Button, Entry, OptionMenu, StringVar
from Processor import Processor
from Memory import Memory
from Snoop import Subscriber, Publisher
from numpy import random
from threading import Thread
import time

class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Proyecto Individual 1")
        master.geometry("800x500")
        self.processorSpeed = 0.1
        self.memorySpeed = 0.2

        self.loop = True

        self.processor = []
        self.subscriber = []
        self.publisher = []

        self.memory = Memory(self.memorySpeed)
        for i in range(4):
            self.processor.append(Processor(i,self.memory,self.processorSpeed))
            self.subscriber.append(Subscriber(self.processor[i]))
            self.publisher.append(Publisher(i))

        #Add Subscribers to Publishers
        self.subscribeToPublisher(self.publisher,self.subscriber)

        #Add processors to the Subscriber
        self.processorToSubscriber(self.processor,self.subscriber)

        #Add publishers to processors
        self.publisherToProcessor(self.processor,self.publisher)




        self.width = 18
        self.height = 1

        #opcion ejecucion continua
        self.ecLabel = Label(master, borderwidth = 2,relief="ridge",text="Ejecucion Continua", width=self.width, height=self.height)
        self.ecStart = Button(master, text="Start", width=self.width , height=self.height, command= lambda: self.instructionFunction(3))
        self.ecStop = Button(master, text="Stop", width=self.width, height=self.height, command = lambda: self.killLoop())

        self.ecLabel.grid(row=0, column=0)
        self.ecStart.grid(row=0, column=1)
        self.ecStop.grid(row=0, column=2)



        #opcion ejecucion loop
        self.elLabel = Label(master, borderwidth = 2,relief="ridge",text="Ejecucion Loop", width=self.width, height=self.height)
        self.elLoop = Entry(master, width=self.width)
        self.elStart = Button(master, text="Start", width=self.width , height=self.height, command= lambda: self.instructionFunction(2))
        self.elLabel.grid(row=1, column=0)
        self.elLoop.grid(row=1, column=1)
        self.elStart.grid(row=1, column=2)



        #opcion ejecucion unitaria
        self.esLabel = Label(master, borderwidth = 2,relief="ridge",text="Ejecucion Unitaria", width=self.width, height=self.height)
        self.esStart = Button(master, text="Start", width=self.width , height=self.height, command = lambda: self.instructionFunction(1))

        self.esLabel.grid(row=2, column=0)
        self.esStart.grid(row=2, column=1)



        #opcion ingresar instruccion
        self.iiLabel = Label(master,borderwidth = 2,relief="ridge", text="Ingresar Instruccion", width=self.width, height=self.height)
        self.processorOption = ["Processor 0", "Processor 1", "Processor 2", "Processor 3"]
        self.processorVar = StringVar(master)
        self.processorVar.set(self.processorOption[0])
        self.pOption = OptionMenu(master,self.processorVar,*self.processorOption)
        self.instructionOption = ["READ", "CALC", "WRITE"]
        self.instructionVar = StringVar(master)
        self.instructionVar.set(self.instructionOption[0])
        self.iOption = OptionMenu(master,self.instructionVar,*self.instructionOption)
        self.iiDireccion = Entry(master, width=self.width)
        self.iiValor = Entry(master, width=self.width)
        self.iiStart = Button(master, text="Start", width=self.width , height=self.height, command= lambda: self.buildInstruction())

        self.iiLabel.grid(row=3, column=0)
        self.pOption.grid(row=3, column=1)
        self.iOption.grid(row=3, column=2)
        self.iiDireccion.grid(row=3, column=3)
        self.iiValor.grid(row=3, column=4)
        self.iiStart.grid(row=3, column=5)

        #Blank
        self.blankLabel1 = Label(master,text="",width=self.width, height=self.height)
        self.blankLabel1.grid(row=4,column=0)

        #Processor 0
        self.p0Label = Label(master,borderwidth = 2,relief="ridge", text="Procesador 0", width=self.width, height=self.height)
        self.p0c0 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p0c1 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p0c2 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p0c3 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p0i = Label(master,borderwidth = 2,relief="raised", text="", width=self.width, height=self.height)

        self.p0Label.grid(row=5, column=0)
        self.p0c0.grid(row=6,column=0)
        self.p0c1.grid(row=7,column=0)
        self.p0c2.grid(row=8,column=0)
        self.p0c3.grid(row=9,column=0)
        self.p0i.grid(row=10,column=0)


        #Processor 1
        self.p1Label = Label(master,borderwidth = 2,relief="ridge", text="Procesador 1", width=self.width, height=self.height)
        self.p1c0 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p1c1 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p1c2 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p1c3 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p1i = Label(master,borderwidth = 2,relief="raised", text="", width=self.width, height=self.height)

        self.p1Label.grid(row=5, column=1)
        self.p1c0.grid(row=6,column=1)
        self.p1c1.grid(row=7,column=1)
        self.p1c2.grid(row=8,column=1)
        self.p1c3.grid(row=9,column=1)
        self.p1i.grid(row=10,column=1)



        #Processor 2
        self.p2Label = Label(master, borderwidth = 2,relief="ridge",text="Procesador 2", width=self.width, height=self.height)
        self.p2c0 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p2c1 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p2c2 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p2c3 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p2i = Label(master,borderwidth = 2,relief="raised", text="", width=self.width, height=self.height)

        self.p2Label.grid(row=5, column=2)
        self.p2c0.grid(row=6,column=2)
        self.p2c1.grid(row=7,column=2)
        self.p2c2.grid(row=8,column=2)
        self.p2c3.grid(row=9,column=2)
        self.p2i.grid(row=10,column=2)



        #Processor 3
        self.p3Label = Label(master, borderwidth = 2,relief="ridge",text="Procesador 3", width=self.width, height=self.height)
        self.p3c0 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p3c1 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p3c2 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p3c3 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p3i = Label(master,borderwidth = 2,relief="raised", text="", width=self.width, height=self.height)

        self.p3Label.grid(row=5, column=3)
        self.p3c0.grid(row=6,column=3)
        self.p3c1.grid(row=7,column=3)
        self.p3c2.grid(row=8,column=3)
        self.p3c3.grid(row=9,column=3)
        self.p3i.grid(row=10,column=3)

        #Instruction Matrix
        self.p0iLabel = Label(master, borderwidth = 2,relief="ridge",text="Procesador 0", width=self.width, height=self.height)
        self.p1iLabel = Label(master, borderwidth = 2,relief="ridge",text="Procesador 1", width=self.width, height=self.height)
        self.p2iLabel = Label(master, borderwidth = 2,relief="ridge",text="Procesador 2", width=self.width, height=self.height)
        self.p3iLabel = Label(master, borderwidth = 2,relief="ridge",text="Procesador 3", width=self.width, height=self.height)

        self.p0iLabel.grid(row=13,column=0)
        self.p1iLabel.grid(row=14,column=0)
        self.p2iLabel.grid(row=15,column=0)
        self.p3iLabel.grid(row=16,column=0)

        self.iLabel = Label(master, borderwidth = 2,relief="ridge",text="Instruccion Ejecutada", width=3*self.width, height=self.height)
        self.p0inst = Label(master, borderwidth = 2,relief="ridge",text="", width=3*self.width, height=self.height)
        self.p1inst = Label(master, borderwidth = 2,relief="ridge",text="", width=3*self.width, height=self.height)
        self.p2inst = Label(master, borderwidth = 2,relief="ridge",text="", width=3*self.width, height=self.height)
        self.p3inst = Label(master, borderwidth = 2,relief="ridge",text="", width=3*self.width, height=self.height)

        self.iLabel.grid(row=12,column=1, columnspan = 3)
        self.p0inst.grid(row=13,column=1, columnspan = 3)
        self.p1inst.grid(row=14,column=1, columnspan = 3)
        self.p2inst.grid(row=15,column=1, columnspan = 3)
        self.p3inst.grid(row=16,column=1, columnspan = 3)


        #Memory
        self.mLabel = Label(master, borderwidth = 2,relief="ridge",text="Memoria", width=self.width, height=self.height)
        self.m0 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m1 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m2 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m3 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m4 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m5 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m6 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m7 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m8 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m9 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m10 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m11 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m12 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m13 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m14 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.m15 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)

        self.mLabel.grid(row=5, column=5)
        self.m0.grid(row=6,column=5)
        self.m1.grid(row=7,column=5)
        self.m2.grid(row=8,column=5)
        self.m3.grid(row=9,column=5)
        self.m4.grid(row=10,column=5)
        self.m5.grid(row=11,column=5)
        self.m6.grid(row=12,column=5)
        self.m7.grid(row=13,column=5)
        self.m8.grid(row=14,column=5)
        self.m9.grid(row=15,column=5)
        self.m10.grid(row=16,column=5)
        self.m11.grid(row=17,column=5)
        self.m12.grid(row=18,column=5)
        self.m13.grid(row=19,column=5)
        self.m14.grid(row=20,column=5)
        self.m15.grid(row=21,column=5)

        self.m0pos = Label(master,borderwidth = 2,relief="ridge", text="0000", width=self.width//3, height=self.height)
        self.m1pos = Label(master,borderwidth = 2,relief="ridge", text="0001", width=self.width//3, height=self.height)
        self.m2pos = Label(master,borderwidth = 2,relief="ridge", text="0010", width=self.width//3, height=self.height)
        self.m3pos = Label(master,borderwidth = 2,relief="ridge", text="0011", width=self.width//3, height=self.height)
        self.m4pos = Label(master,borderwidth = 2,relief="ridge", text="0100", width=self.width//3, height=self.height)
        self.m5pos = Label(master,borderwidth = 2,relief="ridge", text="0101", width=self.width//3, height=self.height)
        self.m6pos = Label(master,borderwidth = 2,relief="ridge", text="0110", width=self.width//3, height=self.height)
        self.m7pos = Label(master,borderwidth = 2,relief="ridge", text="0111", width=self.width//3, height=self.height)
        self.m8pos = Label(master,borderwidth = 2,relief="ridge", text="1000", width=self.width//3, height=self.height)
        self.m9pos = Label(master,borderwidth = 2,relief="ridge", text="1001", width=self.width//3, height=self.height)
        self.m10pos = Label(master,borderwidth = 2,relief="ridge", text="1010", width=self.width//3, height=self.height)
        self.m11pos = Label(master,borderwidth = 2,relief="ridge", text="1011", width=self.width//3, height=self.height)
        self.m12pos = Label(master,borderwidth = 2,relief="ridge", text="1100", width=self.width//3, height=self.height)
        self.m13pos = Label(master,borderwidth = 2,relief="ridge", text="1101", width=self.width//3, height=self.height)
        self.m14pos = Label(master,borderwidth = 2,relief="ridge", text="1110", width=self.width//3, height=self.height)
        self.m15pos = Label(master,borderwidth = 2,relief="ridge", text="1111", width=self.width//3, height=self.height)
        self.m0pos.grid(row=6,column=4,sticky="E")
        self.m1pos.grid(row=7,column=4,sticky="E")
        self.m2pos.grid(row=8,column=4,sticky="E")
        self.m3pos.grid(row=9,column=4,sticky="E")
        self.m4pos.grid(row=10,column=4,sticky="E")
        self.m5pos.grid(row=11,column=4,sticky="E")
        self.m6pos.grid(row=12,column=4,sticky="E")
        self.m7pos.grid(row=13,column=4,sticky="E")
        self.m8pos.grid(row=14,column=4,sticky="E")
        self.m9pos.grid(row=15,column=4,sticky="E")
        self.m10pos.grid(row=16,column=4,sticky="E")
        self.m11pos.grid(row=17,column=4,sticky="E")
        self.m12pos.grid(row=18,column=4,sticky="E")
        self.m13pos.grid(row=19,column=4,sticky="E")
        self.m14pos.grid(row=20,column=4,sticky="E")
        self.m15pos.grid(row=21,column=4,sticky="E")

        self.printMemoryAndCache(self.processorSelector,self.memory)
        
    def subscribeToPublisher(self, publisher, subscribers):
        publisher[0].register(subscribers[1])
        publisher[0].register(subscribers[2])
        publisher[0].register(subscribers[3])
        
        publisher[1].register(subscribers[0])
        publisher[1].register(subscribers[2])
        publisher[1].register(subscribers[3])

        publisher[2].register(subscribers[0])
        publisher[2].register(subscribers[1])
        publisher[2].register(subscribers[3])

        publisher[3].register(subscribers[0])
        publisher[3].register(subscribers[1])
        publisher[3].register(subscribers[2])
        return

    def processorToSubscriber(self, processor, subscribers):
        for i in range(4):
            self.subscriber[i].processorList = processor
        return

    def publisherToProcessor(self, processor, publisher):

        for i in range(4):
            processor[i].Publisher = publisher[i]
        return



#--------------------------------------EXECUTION LOOPS# ---------------------------------

    def generatorSingle(self, instruccion, direccionMemoria,valor):
        self.printMemoryAndCache(self.processor,self.memory)

        p0 = Thread(target=self.mtInstruction, args=(self.processor[0],))
        p1 = Thread(target=self.mtInstruction, args=(self.processor[1],))
        p2 = Thread(target=self.mtInstruction, args=(self.processor[2],))
        p3 = Thread(target=self.mtInstruction, args=(self.processor[3],))

        p0.start()
        p1.start()
        p2.start()
        p3.start()      

        return

    def generatorIteraciones(self, instruccion, direccionMemoria, valor):
        for i in range(int(self.elLoop.get())):

            self.printMemoryAndCache(self.processor,self.memory)

            p0 = Thread(target=self.mtInstruction, args=(self.processor[0],))
            p1 = Thread(target=self.mtInstruction, args=(self.processor[1],))
            p2 = Thread(target=self.mtInstruction, args=(self.processor[2],))
            p3 = Thread(target=self.mtInstruction, args=(self.processor[3],))

            p0.start()
            p1.start()
            p2.start()
            p3.start() 

        return

    def generatorContinous(self, instruccion, direccionMemoria,valor):
        self.loop = True
        while(self.loop):
            
            self.printMemoryAndCache(self.processor,self.memory)

            p0 = Thread(target=self.mtInstruction, args=(self.processor[0],))
            p1 = Thread(target=self.mtInstruction, args=(self.processor[1],))
            p2 = Thread(target=self.mtInstruction, args=(self.processor[2],))
            p3 = Thread(target=self.mtInstruction, args=(self.processor[3],))

            p0.start()
            p1.start()
            p2.start()
            p3.start()

        return

    def killLoop(self):
        self.loop=False
        return
# --------------------------------------------------------------------------------------------

    def mtInstruction(self, processor):
        [instruccion, direccionMemoria, valor] = self.generatorInstruction()
        processor.instruction(instruccion, direccionMemoria, valor)

    def instructionFunction(self, mode):
        [instruccion, direccionMemoria, valor] = self.generatorInstruction()

        if (mode == 1):
            self.generatorSingle(instruccion, direccionMemoria,valor)
        elif (mode == 2):
            self.generatorIteraciones(instruccion, direccionMemoria, valor)
        else:
            self.generatorContinous(instruccion, direccionMemoria,valor)
        
    def generatorInstruction(self):
        instruccion = random.binomial(n=2,p=0.5,size=1)[0]
        direccionMemoria = bin(random.randint(0,15)).replace('0b','')
        valor = hex(random.randint(0,65535)).replace('0x','')
        
        return [instruccion,direccionMemoria,valor]



#-----------------------------------DISPLAY PRINTS--------------------------------------------
    def printMemoryAndCache(self,processor,memory):
        self.p0c0["text"] = self.cacheTextBuilder(self.processor[0].Cache.set0.bloque0)
        self.p0c1["text"] = self.cacheTextBuilder(self.processor[0].Cache.set0.bloque1)
        self.p0c2["text"] = self.cacheTextBuilder(self.processor[0].Cache.set1.bloque0)
        self.p0c3["text"] = self.cacheTextBuilder(self.processor[0].Cache.set1.bloque1)
        self.p0i["text"] = self.processor[0].lastMessage

        self.p1c0["text"] = self.cacheTextBuilder(self.processor[1].Cache.set0.bloque0)
        self.p1c1["text"] = self.cacheTextBuilder(self.processor[1].Cache.set0.bloque1)
        self.p1c2["text"] = self.cacheTextBuilder(self.processor[1].Cache.set1.bloque0)
        self.p1c3["text"] = self.cacheTextBuilder(self.processor[1].Cache.set1.bloque1)
        self.p1i["text"] = self.processor[1].lastMessage

        self.p2c0["text"] = self.cacheTextBuilder(self.processor[2].Cache.set0.bloque0)
        self.p2c1["text"] = self.cacheTextBuilder(self.processor[2].Cache.set0.bloque1)
        self.p2c2["text"] = self.cacheTextBuilder(self.processor[2].Cache.set1.bloque0)
        self.p2c3["text"] = self.cacheTextBuilder(self.processor[2].Cache.set1.bloque1)
        self.p2i["text"] = self.processor[2].lastMessage

        self.p3c0["text"] = self.cacheTextBuilder(self.processor[3].Cache.set0.bloque0)
        self.p3c1["text"] = self.cacheTextBuilder(self.processor[3].Cache.set0.bloque1)
        self.p3c2["text"] = self.cacheTextBuilder(self.processor[3].Cache.set1.bloque0)
        self.p3c3["text"] = self.cacheTextBuilder(self.processor[3].Cache.set1.bloque1)
        self.p3i["text"] = self.processor[3].lastMessage

        self.m0["text"] = self.memory.memGet(0)
        self.m1["text"] = self.memory.memGet(1)
        self.m2["text"] = self.memory.memGet(2)
        self.m3["text"] = self.memory.memGet(3)
        self.m4["text"] = self.memory.memGet(4)
        self.m5["text"] = self.memory.memGet(5)
        self.m6["text"] = self.memory.memGet(6)
        self.m7["text"] = self.memory.memGet(7)
        self.m8["text"] = self.memory.memGet(8)
        self.m9["text"] = self.memory.memGet(9)
        self.m10["text"] = self.memory.memGet(10)
        self.m11["text"] = self.memory.memGet(11)
        self.m12["text"] = self.memory.memGet(12)
        self.m13["text"] = self.memory.memGet(13)
        self.m14["text"] = self.memory.memGet(14)
        self.m15["text"] = self.memory.memGet(15)

        self.p0inst["text"] = self.processor[0].lastInstruction
        self.p1inst["text"] = self.processor[1].lastInstruction
        self.p2inst["text"] = self.processor[2].lastInstruction
        self.p3inst["text"] = self.processor[3].lastInstruction


        return

    def cacheTextBuilder(self,bloqueCache):
        estado = bloqueCache.b_estadoGet()
        direccion = bloqueCache.b_direccionGet()
        dato = bloqueCache.b_datoGet()
        escribir = estado + " - " + direccion + " - " + dato
        return escribir
# --------------------------------------------------------------------------------------------

# -----------------------------------SPECIFIC INSTRUCTION BUILDER-----------------------------
    def buildInstruction(self):
        processorNumber = self.processorSelector(self.processorVar.get())
        instructionNumber = self.instructionSelector(self.instructionVar.get())
        direccionMemoria = bin(int(self.iiDireccion.get(),2)).replace("0b","")
        valor = self.iiValor.get()

        self.processor[processorNumber].instruction(instructionNumber,direccionMemoria,valor)
        self.printMemoryAndCache(self.processor,self.memory)

        if (self.instructionVar.get() == "READ"):
            self.processor[processorNumber].lastInstruction = self.instructionVar.get() + " " + direccionMemoria
        elif (self.instructionVar.get() == "WRITE"):
            self.processor[processorNumber].lastInstruction = self.instructionVar.get() + " " + direccionMemoria + " " + valor
        else:
            self.processor[processorNumber].lastInstruction = self.instructionVar.get()
        return

    def processorSelector(self, processorText):
        if (processorText == "Processor 0"):
            return 0
        elif (processorText == "Processor 1"):
            return 1
        elif (processorText == "Processor 2"):
            return 2
        else:
            return 3
    
    def instructionSelector(self, instructionText):
        if (instructionText == "READ"):
            return 0
        elif (instructionText == "CALC"):
            return 1
        else:
            return 2
# --------------------------------------------------------------------------------------------