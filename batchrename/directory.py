from os import mkdir
from os import listdir
from os import path
from shutil import rmtree


class Directory:

    def __init__(self, root, directory):
        '''Create a directory at the given path.'''
        self.path = str(path.join(root, directory))
        self.files = []

        self.__create(self.path)

    def __create(self, path):
        '''Use this only if something has gone wrong.'''
        if path.exists(path) == False:
            mkdir(path)
        else:
            print(f'A folder named {path.basename(path)} already exists.')

    def delete(self, path):
        '''Delete the given directory.'''
        rmtree(path)

    # Perhaps this should go in the main script.
    def contents(self, path, format=None):
        for entry in os.listidr(self.path):
            if path.isdir(entry):
                continue
            else:    
                if entry[entry.index('.') + 1:] == str(format):
                    self.files.append(entry)
        