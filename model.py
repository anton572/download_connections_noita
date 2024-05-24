import data_worker
from config import config
import os
class model():
    def install_mod(self):
        print(config().get())
        folder=config().get_name("noita_path")+"mods/quant.ew"
        try:
            os.makedirs(folder)
        except:
            pass
        path=[
            "https://github.com/IntQuant/noita_entangled_worlds/releases/download/v0.5.2/quant.ew.zip",
            "https://github.com/IntQuant/noita_entangled_worlds/releases/download/v0.5.2/noita-proxy-win.zip"
        ]
        for i in path:
            data_worker.repackFromgit(i,folder)
    def start_proxy(self):
        folder=config().get_name("noita_path")+"mods/quant.ew/noita_proxy.exe"
        data_worker.run(folder)
    def start_noita(self):
        folder=config().get_name("noita_path")+"noita.exe"
        data_worker.run(folder)
