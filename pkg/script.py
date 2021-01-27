from os import getcwd
from os import mkdir
from os import rename
from os import scandir
from os.path import exists
from os.path import join
from PyPDF2 import PdfFileReader
from queue import Queue
from shutil import copy2
from shutil import move


class Entry:

    def __init__(self, name, path):
        '''Initialize an object representing an entry in a directory.
        
        Attributes:
        name -- the entry's name
        path -- the real file path, starting from the working directory
        '''
        self.name = name
        self.path = join(path, name)

        self.__create()
    
    def __create(self):
        '''Create a new directory with the same name as the object name. '''
        if not exists(self.name):
            try:
                mkdir(self.name)
            except FileExistsError:
                print(f'Found existing folder: {self.name}')

    def __move(self, dst_path):
        '''Move the object to a new directory.'''
        copy2(self.path, dst_path)
        self.path = dst_path

class File(Entry):

        def __init__(self, name, path):
            '''Initialize an entry which is a file.

            Attributes:
            extension -- represents the file's format extension
            metadata -- dictionary which holds the file's metadata
            '''

            Entry.__init__(self, name, path)
            self.path = path
            self.metadata = {}

        def format(self):
            '''Replace characters unusable in the file system.'''
            self.metadata['/Title'] = self.metadata['/Title'].replace(':', ' -')

        def rename(self, backup_path):
            '''Replace the original name with scraped metadata.'''
            try:
                new_title = self.metadata['/Title'] + '.pdf'
                rename(self.name, new_title)
            except KeyError:
                print(f'Metadata import error [RENAME]: {self.name}')

        def scrape(self):
            '''Extract PDF metadata for storage.'''
            with open(self.name, 'rb') as f:
                try:
                    raw_meta = PdfFileReader(f).getDocumentInfo()
                    for key in raw_meta:
                        self.metadata[key] = raw_meta[key]
                except:
                    print(f'Metadata import error [SCRAPE]: {self.name}')
                f.close()

        def title_exists(self):
            '''Check if File.metadata['/Title'] exists and is not empty.'''
            if '/Title' not in self.metadata or self.metadata['/Title'] == '':
                return False
            else:
                return True

def main():

    ROOT = getcwd()
    q = Queue()

    # Create folders required by the script.
    backup = Entry('Backup Files', ROOT)
    missed = Entry('Missed Files', ROOT)

    for entry in scandir():
        if entry.is_file() and entry.name.endswith('.pdf'):
            path = join(ROOT, entry.path[2:])
            copy2(entry.name, backup.path)
            q.put(File(entry.name, path))
        else:
            continue

    # The principal algorithm scrapes each File object here.
    while not q.empty():
        active_file = q.get()
        active_file.scrape()
        
        if not active_file.title_exists():
            move(active_file.path, missed.path)
            continue

        active_file.format()
        try:
            active_file.rename(backup.path)
        except:
            move(active_file.path, missed.path)


if __name__ == "__main__":
    main()