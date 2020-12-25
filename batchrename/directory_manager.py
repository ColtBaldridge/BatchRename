import os
# from pathlib import Path
from shutil import rmtree


# This is the program's install location.
ROOT = os.path.realpath(__file__)


class DirManager:

    def __init__(self):
        # Target is where the files live.
        print('Where are your files located?')
        self.target = input('>>> ')
        pass
    
    '''
    def set_target(self, path):
        os.chdir(path)
        pass
    '''

    def get_files(self, path):
        '''Returns the target file path'''
        return os.listdir(path)

    def hard_reset(self, self.target, backup, missed_files):
        '''In case of catastrophic failure, break glass.'''
        os.remove(self.target)
        os.remove(missed_files)
        os.mkdir(missed_files)
        shutil.copy2(backup, self.target)
        pass

    def move(self, pdf, directory):
        move(pdf, directory)
        pass