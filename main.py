import tkinter
from tkinter.filedialog import askopenfilename
print('conf lode')
from config import config
from tkinter import Button,Label
print('model')
from model import model
class main(tkinter.Tk):
    def __init__(self,model,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.config=config()
        if self.config.get_name("noita_path") == None:
            split_path=[None]
            while split_path[-1]!="noita.exe":
                path=askopenfilename(title = "get noita.exe")
                split_path=path.split('/')

            path='/'.join(split_path[:-1])+'/'
            self.config.set_name("noita_path",path)
            print(self.config.get_name("noita_path"))
        Button(self,text="install mod",command=model.install_mod).pack()
        Button(self,text="start proxy noita",command=model.start_proxy).pack()
        Button(self,text="start noita",command=model.start_noita).pack()


    def run(self):
        self.mainloop()
print('model init')
model=model()
print('root init')
root=main(model)
print('run')
root.run()
