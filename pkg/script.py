import os
from queue import Queue
import shutil



class Entry:

    def __init__(self, name, path):
        '''Initialize an object representing an entry in a directory.
        
        Attributes:
        name -- the entry's name
        path -- the real file path, starting from the working directory
        '''
        self.name = name
        self.path = path

        self.__create()
    
    def __create(self):
        '''Create a new directory with the same name as the object name. '''
        os.mkdir(self.name)


    def __move(self, dst_path):
        '''Move the object to a new directory.'''
        shutil.copy2(self.path, dst_path)

class File(Entry):

        def __init__(self, name):
            '''Initialize an entry which is a file.

            Attributes:
            extension -- represents the file's format extension
            metadata -- dictionary which holds the file's metadata
            '''
            self.extension = name[name.rindex('.') + 1:]
            self.metadata = {}

        def __format(self, name):
            '''Replace characters unusable in the file system.'''
            return name.replace(':', ' -')

        def scrape(self):
            '''Extract PDF metadata for storage.'''
            with open(self.name, 'rb') as f:
                try:
                    self.metadata = PdfFileReader(f).getDocumentInfo()
                except:
                    print(f'Metadata import error [SCRAPE]: {self.name}')

        def rename(self, backup_path):
            '''Replace the original name with scraped metadata.'''
            try:
                formatted_name = format(self.metadata['/Title'])
                os.rename(self.name, formatted_name)
            except KeyError:
                print(f'Metadata import error [RENAME]: {self.name}')
                self.__move(backup_path)

def main():

    # First, create some basic data required by the script:
    
    # ROOT represents the working directory. This is passed to Entry
    #  objects to establish object paths.
    ROOT = os.getcwd()
    
    # The queue stores the target files for editing.
    q = Queue()

    # Before touching anything, first back up everything.
    backup = Entry('Backup Files', ROOT)

    # Implement some list iterator for file contents

    # With everything set up, scan the active directory for PDfs.
    for entry in os.scandir():
        # Make sure the entry is in fact both a file and a PDF.
        if entry.is_file():
            # Create a File object to represent the PDF and enqueue.
            q.put(File(entry.name, entry.path))
            pass


    # The principal algorithm scrapes each File object here.
    while not q.empty():
        active_file = q.get()
        active_file.scrape()
        try:
            active_file.rename(backup.path)
        except:
            shutil.copy2(active_file.name, 'Backup Files')        
        pass
    
    

if __name__ == "__main__":
    main()