class packer():
    @staticmethod
    def pack(data):
        st=str(data)
        if type(data)==str:
            return "'{}'".format(st)
        return st
    @staticmethod
    def repack(data):
        if "'" in data:
            return data[1:-1]

        try:
            _int=int(data)
            return _int
        except:
            pass
class config():
    __exemple=None
    def __new__(cls):
        if cls.__exemple==None:
            cls.__exemple=super().__new__(cls)
        return cls.__exemple

    def __init__(self,init={"noita_path":None}):
        self.__init=init
        self.name_file='config.conf'
        try:
            self.__set_r()
        except FileNotFoundError:
            self.return_initial_state()
    def return_initial_state(self):
        self.set(self.__init)
    def set(self,stait:dict):
        self.__set_w()
        _s=''
        for i in stait:
            pack=packer.pack(stait[i])
            _s+="{}={}\n".format(i,pack)
        self.__File.write(_s)
    def get(self):
        self.__set_r()
        data={}
        filestr=self.__File.read()

        for i in filestr.split('\n')[:-1]:

            line=i.split('=',2)
            data[line[0]]=packer.repack(line[1])
        return data
    def get_name(self,name):
        return self.get()[name]
    def set_name(self,name,val):
        staite=self.get()
        staite[name]=val
        self.set(staite)
    def __set_w(self):
        try:
            if self.__File.mode=='w':
                self.__File.seek(0)
                return None
            self.__File.close()
        except AttributeError:
            pass
        self.__File=open(self.name_file,'w')

        print('w')
    def __set_r(self):
        try:
            if self.__File.mode=='r':
                self.__File.seek(0)
                return None
            self.__File.close()
        except AttributeError:
            pass
        self.__File=open(self.name_file,'r')
        print('r')
    def __del__(self):
        self.__File.close()
if __name__ =="__main__":
    conf=config()
    conf.set_name("noita_path",None)
    conf2=config()
    print(conf2.get())
