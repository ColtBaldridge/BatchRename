from os import path
from os import listdir
from os import scandir
from PyDPF2 import PdfFileReader
from shutil import copy2


class Directory:



    def __init__(self, root, name):
        self.name = name
        self.path = path.listdir(root, name)

        self.__create()

    def __create(self):
        '''Use this only if something has gone wrong.'''
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        else:
            print(f'Found existing folder {self.name}.')

    def delete(self):
        '''Delete the given directory.'''
        rmtree(self.path)


class File:
    

    def __init__(self, name, path):
        self.name = name
        self.extension name[name.rindex('.') + 1:]
        self.metadata = {}
        self.path = path

    def scrape(self):
        with open(self.name, 'rb') as f:
            try:
                self.metadata = PdfFileReader(f).getDocumentInfo()
            except:
                pass
                # Either use move() method or shutil.copy2()
    
    def format(self):
        self.name.replace(':', ' -')