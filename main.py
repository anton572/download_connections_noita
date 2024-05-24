import tkinter
from tkinter.filedialog import askopenfilename
from config import config
from tkinter import Button,Label
from model import model
class main(tkinter.Tk):
    def __init__(self,model,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.config=config()
        if self.config.get_name("noita_path") == None:
            path=askopenfilename(
                initialdir = "C:\\",title = "get noita.exe")
            path='/'.join(path.split('/')[:-1])+'/'
            self.config.set_name("noita_path",path)
            print(self.config.get_name("noita_path"))
        Button(self,text="install mod",command=model.install_mod).pack()
        Button(self,text="start proxy noita",command=model.start_proxy).pack()
        Button(self,text="start noita",command=model.start_noita).pack()


    def run(self):
        self.mainloop()

if __name__ =="__main__":
    model=model()
    root=main(model)
    root.run()
