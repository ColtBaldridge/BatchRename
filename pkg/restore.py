from os import mkdir
from pathlib import Path
from shutil import rmtree
from shutil import copy2
from shutil import copytree
from time import sleep


def status(message):
    '''Status notification system.'''
    print(f'{message}...')
    sleep(1.0)


def main():
    
    # Define essential paths.
    lab = Path('test/lab')
    backup = Path('test/docs')

    # Remove test/lab and then create a new copy.
    status('Cleaning test/lab/')
    if lab.exists():
        rmtree(lab)

    # Create a new lab folder.
    status('Restoring from backup')
    copytree(backup, lab)

    # Deploy the latest version of script.py to the lab.
    copy2('script.py', lab)

if __name__ == '__main__':
    main()