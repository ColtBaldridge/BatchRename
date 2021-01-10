from os import mkdir
from pathlib import Path
from shutil import rmtree
from shutil import copy2
from shutil import copytree


def main():
    
    # Define essential paths.
    lab = Path('test/lab')
    backup = Path('test/docs')

    # Remove test/lab and then create a new copy.
    if lab.exists():
        rmtree(lab)
    copytree(backup, lab)

    # Deploy the latest version of script.py to the lab.
    copy2('script.py', lab)

if __name__ == '__main__':
    main()