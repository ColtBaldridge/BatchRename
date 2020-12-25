import os
from shutil import rmtree


class Directory:
    
    def __init__(self, root, directory):
        '''Create a directory at the given path.'''
        self.path = os.path.join(root, directory)
        self.name = directory
        self.files = []
        self.exceptions = []
        
        self.__create()

    def __create(self):
        '''Use this only if something has gone wrong.'''
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        else:
            print(f'Found existing folder {self.name}.')
    
    def __get_extension(self, file): 
        # Look into implementing str.rindex() for files with periods in their title.
        return file[file.index('.') + 1:]

    def delete(self):
        '''Delete the given directory.'''
        rmtree(self.path)

    # Perhaps this should go in the main script.
    def contents(self, format=None):
        for entry in os.listdir(self.name):
            if not os.path.isdir(os.path.join(self.path, entry)):
                # print(f'Fetching file exention of {entry}')
                try:
                    if self.__get_extension(entry) == str(format):
                        self.files.append(entry)
                    else:
                        self.exceptions.append(entry)
                except:
                    print(f'\nSubstring not found for {entry} (index: {os.listdir(self.name).index(entry)})')
            else:
                self.exceptions.append(entry)