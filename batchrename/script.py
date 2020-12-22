import os
from PyPDF2 import PdfFileReader
from directory import Directory
import shutil
from sys import modules

def setup():
    '''
    Required modules:
        os
        pathlib
        shutil
        PyPDF2
    '''
    pass

print('Enter the directory path to the target files.')
ROOT = str(input('>>> '))

# If the script ends up being a single file use this line instead.
ROOT = os.path.realpath(__file__)


def main():
    
    backup = Directory(ROOT, 'Backup')
    missed = Directory(ROOT, 'Missed Files')

    # This exists solely to shut up the interpreter.
    print(backup + missed)


if __name__ == "__main__":
    main()