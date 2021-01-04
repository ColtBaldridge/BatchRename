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
import time


ROOT = Path(os.getcwd())


def main():

    # Constants
    production = 'reading-list'
    backup = 'reading-list-backup'

    print(f'Removing all contents from {production}')
    shutil.rmtree(production)
    print(f'Restoring {production} from backup...')
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