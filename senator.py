import tkinter
class abc():
    def __init__(self):
        self.pencerem=tkinter.Tk()
        self.metin=tkinter.StringVar()
        self.giriş=tkinter.Entry(self.pencerem,textvariable=self.metin)
        self.giriş.pack()
        self.düğme=tkinter.Button(self.pencerem,text="ara",command=self.ara)
        self.düğme.pack()
        self.listetut=tkinter.StringVar()
        self.listeboxim=tkinter.Listbox(self.pencerem,listvariable=self.listetut)
        self.listeboxim.pack()
        
        
        tkinter.mainloop()
    def ara(self):
        
        self.listem=[]
        self.dosyam=open("senator.txt","r")
        for line in self.dosyam:
            line=line.rstrip()
            line=line.split(",")
            if self.metin.get()==line[1]:
                self.listem.append(line[0]+line[2])
        self.dosyam.close()
        self.listetut.set(tuple(self.listem))
        self.metin.set("")

x=abc()     


        
        

        




        


      
                




        
    
                


        
             


            
    
        
       
        






