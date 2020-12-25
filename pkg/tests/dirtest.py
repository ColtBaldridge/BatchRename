import os
from directory import Directory
import time


def main():
    '''This script tests directory.py for bugs.'''

    print('Setting the root directory path', end='\n\n')
    time.sleep(0.5)
    root = os.getcwd()

    print('Creating directory object \'target\'', end='\n\n')
    time.sleep(0.5)
    target = Directory(root, 'reading-list')

    print('Grabbing files from target', end='\n\n')
    time.sleep(0.5)
    
    target.contents(format='pdf')
    
    print()

    print(f'Sucessfully added {len(target.files)}/\
        {len(os.listdir(target.name))} entries to queue.', end='\n\n')
    print(f'Failed to add {len(target.exceptions)} files to queue:'\
        , end='\n\n')
    for entry in target.exceptions:
        print(entry)

if __name__ == '__main__':
    main()