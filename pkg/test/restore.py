from os import mkdir
from pathlib import Path
from shutil import rmtree
from shutil import copy2
from shutil import copytree


def main():
    
    # Define essential paths`
    lab = Path('tests/lab')
    backup = Path('tests/docs')

    if lab.exists():
        rmtree(lab)
    copytree(backup, lab)
    copy2('script.py', lab)

if __name__ == '__main__':
    main()