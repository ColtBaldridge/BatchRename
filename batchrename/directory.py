import os
from shutil import rmtree


class Directory:

    def __init__(self, root, directory):
        '''Create a directory at the given path.'''
        self.directory = str(os.path.join(root, directory))
        os.mkdir(self.directory)

    def create(self, path):
        '''Use this only if something has gone wrong.'''
        if os.path.exists(path) == False:
            os.mkdir(path)
        else:
            print(f'A folder named {os.path.basename(path)} already exists.')

    def delete(self, path):
        '''Delete the given directory.'''
        rmtree(path)