from tkinter import Tk, Label, Button, Entry, OptionMenu, StringVar


class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Proyecto Individual 1")
        master.geometry("800x500")

        self.width = 18
        self.height = 1

        #opcion ejecucion continua
        self.ecLabel = Label(master, borderwidth = 2,relief="ridge",text="Ejecucion Continua", width=self.width, height=self.height)
        self.ecStart = Button(master, text="Start", width=self.width , height=self.height)
        self.ecStop = Button(master, text="Stop", width=self.width, height=self.height)

        self.ecLabel.grid(row=0, column=0)
        self.ecStart.grid(row=0, column=1)
        self.ecStop.grid(row=0, column=2)



        #opcion ejecucion loop
        self.elLabel = Label(master, borderwidth = 2,relief="ridge",text="Ejecucion Loop", width=self.width, height=self.height)
        self.elLoop = Entry(master, width=self.width)
        self.elStart = Button(master, text="Start", width=self.width , height=self.height)

        self.elLabel.grid(row=1, column=0)
        self.elLoop.grid(row=1, column=1)
        self.elStart.grid(row=1, column=2)



        #opcion ejecucion unitaria
        self.esLabel = Label(master, borderwidth = 2,relief="ridge",text="Ejecucion Unitario", width=self.width, height=self.height)
        self.esStart = Button(master, text="Start", width=self.width , height=self.height)

        self.esLabel.grid(row=2, column=0)
        self.esStart.grid(row=2, column=1)



        #opcion ingresatr instruccion
        self.iiLabel = Label(master,borderwidth = 2,relief="ridge", text="Ingresar Instruccion", width=self.width, height=self.height)
        processorOption = ["Processor 0", "Processor 1", "Processor 2", "Processor 3"]
        processorVar = StringVar(master)
        processorVar.set(processorOption[0])
        self.pOption = OptionMenu(master,processorVar,*processorOption)
        instructionOption = ["READ", "CALC", "WRITE"]
        instructionVar = StringVar(master)
        instructionVar.set(instructionOption[0])
        self.iOption = OptionMenu(master,instructionVar,*instructionOption)
        self.iiDireccion = Entry(master, width=self.width)
        self.iiValor = Entry(master, width=self.width)
        self.iiStart = Button(master, text="Start", width=self.width , height=self.height)

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

        self.p0Label.grid(row=5, column=0)
        self.p0c0.grid(row=6,column=0)
        self.p0c1.grid(row=7,column=0)
        self.p0c2.grid(row=8,column=0)
        self.p0c3.grid(row=9,column=0)


        #Processor 1
        self.p1Label = Label(master,borderwidth = 2,relief="ridge", text="Procesador 1", width=self.width, height=self.height)
        self.p1c0 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p1c1 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p1c2 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p1c3 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)

        self.p1Label.grid(row=5, column=1)
        self.p1c0.grid(row=6,column=1)
        self.p1c1.grid(row=7,column=1)
        self.p1c2.grid(row=8,column=1)
        self.p1c3.grid(row=9,column=1)



        #Processor 2
        self.p2Label = Label(master, borderwidth = 2,relief="ridge",text="Procesador 2", width=self.width, height=self.height)
        self.p2c0 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p2c1 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p2c2 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p2c3 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)

        self.p2Label.grid(row=5, column=2)
        self.p2c0.grid(row=6,column=2)
        self.p2c1.grid(row=7,column=2)
        self.p2c2.grid(row=8,column=2)
        self.p2c3.grid(row=9,column=2)



        #Processor 3
        self.p3Label = Label(master, borderwidth = 2,relief="ridge",text="Procesador 3", width=self.width, height=self.height)
        self.p3c0 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p3c1 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p3c2 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)
        self.p3c3 = Label(master,borderwidth = 2,relief="ridge", text="", width=self.width, height=self.height)

        self.p3Label.grid(row=5, column=3)
        self.p3c0.grid(row=6,column=3)
        self.p3c1.grid(row=7,column=3)
        self.p3c2.grid(row=8,column=3)
        self.p3c3.grid(row=9,column=3)

        #Blank
        self.blankLabel2 = Label(master,text="",width=self.width, height=self.height)
        self.blankLabel2.grid(row=10,column=0)

        #Instruction Matrix
        self.p0iLabel = Label(master, borderwidth = 2,relief="ridge",text="Procesador 0", width=self.width, height=self.height)
        self.p1iLabel = Label(master, borderwidth = 2,relief="ridge",text="Procesador 1", width=self.width, height=self.height)
        self.p2iLabel = Label(master, borderwidth = 2,relief="ridge",text="Procesador 2", width=self.width, height=self.height)
        self.p3iLabel = Label(master, borderwidth = 2,relief="ridge",text="Procesador 3", width=self.width, height=self.height)

        self.p0iLabel.grid(row=12,column=0)
        self.p1iLabel.grid(row=13,column=0)
        self.p2iLabel.grid(row=14,column=0)
        self.p3iLabel.grid(row=15,column=0)

        self.iLabel = Label(master, borderwidth = 2,relief="ridge",text="Instruccion Ejecutada", width=3*self.width, height=self.height)
        self.p0inst = Label(master, borderwidth = 2,relief="ridge",text="", width=3*self.width, height=self.height)
        self.p1inst = Label(master, borderwidth = 2,relief="ridge",text="", width=3*self.width, height=self.height)
        self.p2inst = Label(master, borderwidth = 2,relief="ridge",text="", width=3*self.width, height=self.height)
        self.p3inst = Label(master, borderwidth = 2,relief="ridge",text="", width=3*self.width, height=self.height)

        self.iLabel.grid(row=11,column=1, columnspan = 3)
        self.p0inst.grid(row=12,column=1, columnspan = 3)
        self.p1inst.grid(row=13,column=1, columnspan = 3)
        self.p2inst.grid(row=14,column=1, columnspan = 3)
        self.p3inst.grid(row=15,column=1, columnspan = 3)


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
        


root = Tk()
gui = GUI(root)
root.mainloop()