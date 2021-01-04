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
import os
import shutil
from os import getcwd
from os import mkdir
from os import path
from os import scandir
from shutil import copytree
from shutil import rmtree
import time


ROOT = Path(os.getcwd())


def main():

    # Constants
    production = 'reading-list'
    backup = 'reading-list-backup'

    print('Restoring PDF directory from the backup...')
    shutil.rmtree(production)
    shutil.copytree(backup, production)

    time.sleep(0.5)

    # Lambdas
    verify_contents = lambda src, dst : os.scandir(src) == os.scandir(dst)

    print('Checking the restoration validity...', end='')
    if verify_contents(backup, production):
        print('Success!')
    else:
        print('Coppy Error')


if ROOT.name == 'pkg' and __name__ == '__main__':
    main()
