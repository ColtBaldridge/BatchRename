from os import mkdir
from pathlib import Path
from shutil import rmtree
from shutil import copy2
from shutil import copytree
from time import sleep


def main():
    
    # Define essential paths.
    lab = Path('test/lab')
    backup = Path('test/docs')

    # Remove test/lab and then create a new copy.
    print('Detecting test/lab', end='')
    sleep(0.5)
    if lab.exists():
        rmtree(lab)
    print('Done.')

    # Create a new lab folder.
    print('Restoring from backup...', end='')
    copytree(backup, lab)
    print('Done.')
    sleep(0.5)

    # Deploy the latest version of script.py to the lab.
    copy2('script.py', lab)

if __name__ == '__main__':
    main()