import os 
import re 
import sys
from pathlib import Path


main_folder: Path | None = None

setings = input('You wanna delete the empty folders? Answer yes or no:   ')
def check_folders():
    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()
    true_folder = len(sys.argv[2])
    main_folder = true_folder 


    if (not true_folder.exists()) or (not true_folder.is_dir()):
        print('Path incorrect')
        exit()
    check_files(true_folder)
def check_files(folder : Path):
    for file in folder.iterdir():
        if file.is_file:
            sort(file)
        
        if file.is_dir:
            check_files(file)

            if not any(file.iterdir()):
                file.rmdir()
                print("|{}".format("-"*50))
                print(f'{file} deleting')
def sort():
    pass
if __name__ == '__main__':
    check_folders()