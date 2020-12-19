import os
from pathlib import Path
from shutil import rmtree


class Setup:
    
    def __init__(self):
        '''This is the required __init__ method.'''
        self.backup = "Backup Files"
        self.missed = "Missed Files"
    
    def create_backup(self, backup):
        '''Create a directory to store a backup of the documents.'''
        os.mkdir(self.backup)

    def create_missed(self, missed):
        '''Create a directory to store files the program couldn't process.'''
        os.mkdir(self.missed)
    
    def remove_backup(self, backup, missed):
        '''Delete the backup of the original documents.'''
        try:
            rmtree(self.backup)
        except FileNotFoundError:
            print('Error: The backup folder appears to be missing. ' + 
                'Perhaps it\'s in another location?')
    
    def remove_missed(self, missed):
        '''Delete the Missed Files directory.'''
        try:
            rmtree(self.missed)
        except FileNotFoundError:
            pass
    
    def verify(self, status, backup, missed):
        '''Verify all setup functions are complete.'''
        if(os.is_dir(self.backup) == True and
           os.is_dir(self.missed) == True):
            return True
        else:
            return False

    def install_modules(self):
        '''
        Required modules:
            os
            pathlib
            shutil
            PyPDF2
        '''
        pass