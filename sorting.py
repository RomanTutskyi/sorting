import os
import sys
from pathlib import Path
import re
import time

EXTENTIONS = {
    'images': ('.jpeg', '.png', '.jpg', '.svg', '.dng'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'documents': ('.doc', '.docx', '.txt', '.pdf', '.xls', '.xlsx', '.pptx', '.djvu', '.rtf'),
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'archives': ('.zip', '.gz', '.tar'),
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"

TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

main_folder: Path | None = None

def check_path():
    
    global main_folder

    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()

    true_folder = Path(sys.argv[1])
    

    if (not true_folder.exists()) or (not true_folder.is_dir()):
        print('Path incorrect')
        exit()

    main_folder = true_folder
    
    check_files(true_folder)

def check_files(folder: Path):
    for file in folder.iterdir():

        if file.is_file():
            
            sort(file)
            
        if file.is_dir():
            
            check_files(file)
            

            if not any(file.iterdir()):
                file.rmdir()
                print(f'{file} deleting')

def sort(file: Path):
    path = Path(file)
    file_suffix = file.suffix.lower()
    
    file_name = file.stem
    zero_station = 0
     
    for key, values in EXTENTIONS.items():
        if file_suffix in values:
            zero_station = key 
    if zero_station != 0: 
        
        new_file_name = file_name + file_suffix
        
        end_folder = main_folder.joinpath(zero_station)

        
        end_folder.mkdir(exist_ok=True)
        new_file_path = end_folder.joinpath(new_file_name) 
        try:
            file.rename(new_file_path)
        except FileExistsError:
            time_stamp = time.time()
            new_file_path = end_folder.joinpath (file_name + '_' + str(time_stamp) + file_suffix)
            file.rename(new_file_path)
    else:
        
        new_file_name = file_name + file_suffix
        
        end_folder = main_folder.joinpath('Another')

        
        end_folder.mkdir(exist_ok=True)
        new_file_path = end_folder.joinpath(new_file_name) 
        try:
            file.rename(new_file_path)
        except FileExistsError:
            time_stamp = time.time()
            new_file_path = end_folder.joinpath(file_name + '_' + str(time_stamp) + file_suffix)
            file.rename(new_file_path)


if __name__ == '__main__':
    
    check_path()
    print("|{}".format("*"*50))
    print("|Done!! |")
    print("|{}".format("*"*50))