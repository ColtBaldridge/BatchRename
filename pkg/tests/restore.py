# This script resets the repository through the following:
# 
# 1) Delete reading-list
# 2) Make a copy of reading-list-backup
# 3) Rename reading-list-backup (copy) to reading-list
# 
# Alternatively:
# 1) Delete all enetries at reading-list/*
# 2) copy reading-list-backup reading-list


from pathlib import Path
from os import getcwd
from os import mkdir
from os import path
from os import scandir
from shutil import copytree
from shutil import rmtree
import time


ROOT = Path(getcwd())


def main():

    # Constants
    production = 'reading-list'
    backup = 'reading-list-backup'

    # Lambdas
    verify_contents = lambda src, dst : scandir(src) == scandir(dst)

    print('Restoring PDF directory from the backup...')
    rmtree(production)
    copytree(backup, production)

    time.sleep(0.5)

    print('Checking the restoration validity...', end='')
    if verify_contents(backup, production):
        print('Success!')
    else:
        print('Coppy Error')
        # print('Initiating scan...')
        # 
        # time.sleep(0.5)
        # 
        # for         


if ROOT.name == 'pkg' and __name__ == '__main__':
    main()
