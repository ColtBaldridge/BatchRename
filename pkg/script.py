import os
from queue import Queue
import shutil



class File:
    

    def __init__(self, name, path):
        self.name = name
        self.extension = name[name.rindex('.') + 1:]
        self.metadata = {}
        self.path = path
    
    def __format(self, name):
        return name.replace(':', ' -')

    def scrape(self):
        with open(self.name, 'rb') as f:
            try:
                self.metadata = PdfFileReader(f).getDocumentInfo()
            except:
                print(f'Metadata import error [SCRAPE]: {self.name}')

    def rename(self, backup_path):
        try:
            formatted_name = format(self.metadata['/Title'])
            os.rename(self.name, formatted_name)
        except KeyError:
            print(f'Metadata import error [RENAME]: {self.name}')
            self.__move(backup_path)

    def __move(self, dst_path):
        shutil.copy2(self.path, dst_path)


def main():

    ROOT = os.getcwd()
    q = Queue()
    os.mkdir('Backup Files')

    # Implement some list iterator for file contents

    for entry in os.scandir():
        if entry.is_file():
            # objectFile.scrape()
            pass


    # The principal algorithm scrapes each File object here.
    while not q.empty():
        active_file = q.get()
        try:
            active_file.rename(backup.path)
        except:
            shutil.copy2(active_file.name, 'Backup Files')        
        pass
    
    

if __name__ == "__main__":
    main()